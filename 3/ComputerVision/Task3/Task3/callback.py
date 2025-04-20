# import the necessary packages
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.utils import array_to_img
from tensorflow import random
import matplotlib.pyplot as plt
import os

class GANMonitor(Callback):
	def __init__(self, output_img_path, output_model_path, 
		num_img=3, latent_dim=100):
		# define the number of images and the latent dimension
		self.num_img = num_img
		self.latent_dim = latent_dim

		# define the seed for visualization
		self.seed = random.normal([16, latent_dim])

		# define the output path to store images and model
		self.output_img_path = output_img_path
		self.output_model_path = output_model_path

	def on_epoch_end(self, epoch, logs=None):
		# generate images from the random noise and denormalize them
		generated_images = self.model.generator(self.seed)
		generated_images = (generated_images * 127.5) + 127.5
		generated_images.numpy()

		plt.figure(figsize=(4, 4))
		# iterate over the subplots and display the generated images
		for i in range(self.num_img):
			plt.subplot(4, 4, i+1)
			img = array_to_img(generated_images[i]) 
			plt.imshow(img, cmap="gray")
			plt.axis("off")
		
		# define the output path and save the images
		output_file = os.path.join(
			self.output_img_path, f"epoch_{epoch:03d}.png")	
		plt.savefig(output_file)
		plt.show()

	def on_train_end(self, logs=None):
		# define the output path to store the generator model and save
		# the generator model
		output_file = os.path.join(
			self.output_model_path, "generator.h5")
		self.model.generator.save(output_file)