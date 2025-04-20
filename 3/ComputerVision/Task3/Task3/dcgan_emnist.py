# USAGE
# python dcgan_fashion_mnist.py -o output -e 10 -b 32 -l 100 -c 1

# import the necessary packages
from dcgan import DCGAN
from callback import GANMonitor
from model import get_generator
from model import get_discriminator
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras.optimizers import Adam
import tensorflow_datasets as tfds
import tensorflow as tf
import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory")
ap.add_argument("-e", "--epochs", type=int, default=50,
	help="# epochs to train for")
ap.add_argument("-b", "--batch-size", type=int, default=32,
	help="batch size for training")
ap.add_argument("-l", "--latent-dim", type=int, default=100,
	help="latent dimension of the random noise")
ap.add_argument("-c", "--channels", type=int, default=1,
	help="number of channels of image")
args = vars(ap.parse_args())

# store the epochs and batch size in convenience variables
NUM_EPOCHS = args["epochs"]
BATCH_SIZE = args["batch_size"]

# set the latent dimension of random noise and number of channels of
# the images
LATENT_DIM = args["latent_dim"]
CHANNELS = args["channels"]

# Load 'emnist/byclass' or another variant like 'emnist/letters'
ds = tfds.load('emnist/byclass', split='train', as_supervised=True)

# Preprocess the dataset
def preprocess(image, label):
    image = tf.cast(image, tf.float32)
    image = (image - 127.5) / 127.5  # Normalize to [-1, 1]
    image = tf.expand_dims(image, -1)  # Make sure shape is (28, 28, 1)
    return image

ds = ds.map(lambda img, lbl: preprocess(img, lbl)).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

# define a weight initializer for the generator
GENERATOR_WEIGHT_INIT = RandomNormal(mean=0.0, stddev=0.02)

# build the generator
print("[INFO] building generator...")
gen = get_generator(weight_init=GENERATOR_WEIGHT_INIT,
	latent_dim=LATENT_DIM, channels=CHANNELS)

# build the discriminator
print("[INFO] building discriminator...")
disc = get_discriminator(28, 28, 1)

# build the DCGAN Trainer model and compile the model with the suitable
# optimizers and loss functions
print("[INFO] building the dcgan trainer...")
dcgan = DCGAN(discriminator=disc, generator=gen,
	latent_dim=LATENT_DIM, batch_size=BATCH_SIZE)
dcgan.compile(d_optimizer=Adam(learning_rate=2e-4, beta_1=0.5),
	g_optimizer=Adam(learning_rate=2e-4, beta_1=0.5),
	loss_fn=BinaryCrossentropy())

# check whether the output folder is already present, if not create
# the output folder
OUTPUT_DIR = args["output"]
OUTPUT_IMAGE_DIR = os.path.join(OUTPUT_DIR, "images")
OUTPUT_MODEL_DIR = os.path.join(OUTPUT_DIR, "model")
if not os.path.exists(OUTPUT_DIR):
	os.makedirs(OUTPUT_IMAGE_DIR)
	os.makedirs(OUTPUT_MODEL_DIR)

# create an instance of the gan monitor callback and train the dcgan
# trainer with the training images
print("[INFO] training the dcgan trainer...")
gan_monitor = GANMonitor(output_img_path=OUTPUT_IMAGE_DIR,
	output_model_path=OUTPUT_MODEL_DIR, num_img=16,
	latent_dim=LATENT_DIM)
dcgan.fit(ds, epochs=NUM_EPOCHS, callbacks=[gan_monitor])
