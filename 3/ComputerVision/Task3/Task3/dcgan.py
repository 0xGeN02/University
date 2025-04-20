# import the necessary packages
from tensorflow.keras.metrics import Mean
from tensorflow import GradientTape
from tensorflow.keras import Model
from tensorflow import random
import tensorflow as tf

class DCGAN(Model):
	def __init__(self, discriminator, generator, latent_dim, 
		batch_size):
		super().__init__()
		# get the discriminator, generator and the latent dimensions
		self.discriminator = discriminator
		self.generator = generator
		self.latent_dim = latent_dim

		# initialize the loss metrics
		self.d_loss_metric = Mean(name="d_loss")
		self.g_loss_metric = Mean(name="g_loss")

		# initialize the batch size
		self.batch_size = batch_size

	def compile(self, d_optimizer, g_optimizer, loss_fn):
		super().compile()
		# get the optimizers for the generator and the discriminator
		self.d_optimizer = d_optimizer
		self.g_optimizer = g_optimizer

		# get the loss function
		self.loss_fn = loss_fn

	@property
	def metrics(self):
		# return the loss metrics
		return [self.d_loss_metric, self.g_loss_metric]

	def train_step(self, real_images):
		# build a noise vector of shape (batch_size, latent_dim)
		noise = random.normal(
			shape=(self.batch_size, self.latent_dim))

		# Step 1. Train the discriminator with both real images
		# (label as 1) and fake images (label as 0) 
		with GradientTape() as tape:
			# Compute discriminator loss on real images
			pred_real = self.discriminator(real_images, training=True)
			d_loss_real = self.loss_fn(
				tf.ones((self.batch_size, 1)), pred_real)

			# compute discriminator loss on fake images
			fake_images = self.generator(noise, training=True)
			pred_fake = self.discriminator(fake_images, training=True)
			d_loss_fake = self.loss_fn(
				tf.zeros((self.batch_size, 1)), pred_fake)

			# total discriminator loss
			d_loss = (d_loss_real + d_loss_fake)/2
		
		# compute discriminator gradients and update the trainiable
		# varaibles
		disc_train_vars = self.discriminator.trainable_variables
		grads = tape.gradient(d_loss, disc_train_vars)
		self.d_optimizer.apply_gradients(zip(grads, disc_train_vars))

		# Step 2. Train the generator (do not update weights of the
		# discriminator) G wants D to think the fake images are
		# real (label as 1)
		misleading_labels = tf.ones((self.batch_size, 1)) 
		with GradientTape() as tape:
			fake_images = self.generator(noise, training=True)
			pred_fake = self.discriminator(fake_images, training=True)
			g_loss = self.loss_fn(misleading_labels, pred_fake)
		
		# compute generator gradients and update the trainable
		# variables
		gen_train_vars = self.generator.trainable_variables
		grads = tape.gradient(g_loss, gen_train_vars)
		self.g_optimizer.apply_gradients(zip(grads, gen_train_vars))

		self.d_loss_metric.update_state(d_loss)
		self.g_loss_metric.update_state(g_loss)

		# return the generator and discrimiator loss
		return {"d_loss": self.d_loss_metric.result(),
			"g_loss": self.g_loss_metric.result()}