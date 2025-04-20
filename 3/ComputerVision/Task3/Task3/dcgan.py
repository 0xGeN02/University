# import the necessary packages
from tensorflow.keras.metrics import Mean
from tensorflow import GradientTape
from tensorflow.keras import Model
from tensorflow import random
import tensorflow as tf

from tensorflow.keras.metrics import Mean
from tensorflow import GradientTape
from tensorflow.keras import Model
from tensorflow import random
import tensorflow as tf

class DCGAN(Model):
    def __init__(self, discriminator, generator, latent_dim, batch_size):
        super().__init__()
        self.discriminator = discriminator
        self.generator = generator
        self.latent_dim = latent_dim
        self.batch_size = batch_size

        # initialize loss metrics
        self.d_loss_metric = Mean(name="d_loss")
        self.g_loss_metric = Mean(name="g_loss")

    def compile(self, d_optimizer, g_optimizer, loss_fn):
        super().compile()
        self.d_optimizer = d_optimizer
        self.g_optimizer = g_optimizer
        self.loss_fn = loss_fn

    @property
    def metrics(self):
        return [self.d_loss_metric, self.g_loss_metric]

    def train_step(self, real_images):
        # determine current batch size (handles last partial batch)
        cur_bs = tf.shape(real_images)[0]

        # build noise and label vectors for this batch
        noise = random.normal(shape=(cur_bs, self.latent_dim))

        # 1. Train discriminator on real and fake images
        with GradientTape() as tape:
            # real images
            pred_real = self.discriminator(real_images, training=True)
            d_loss_real = self.loss_fn(
                tf.ones((cur_bs, 1)), pred_real)

            # fake images
            fake_images = self.generator(noise, training=True)
            pred_fake = self.discriminator(fake_images, training=True)
            d_loss_fake = self.loss_fn(
                tf.zeros((cur_bs, 1)), pred_fake)

            d_loss = (d_loss_real + d_loss_fake) / 2

        grads_d = tape.gradient(d_loss, self.discriminator.trainable_variables)
        self.d_optimizer.apply_gradients(zip(grads_d, self.discriminator.trainable_variables))

        # 2. Train generator (wants discriminator to output "real" for fakes)
        misleading_labels = tf.ones((cur_bs, 1))
        with GradientTape() as tape:
            fake_images = self.generator(noise, training=True)
            pred_fake = self.discriminator(fake_images, training=True)
            g_loss = self.loss_fn(misleading_labels, pred_fake)

        grads_g = tape.gradient(g_loss, self.generator.trainable_variables)
        self.g_optimizer.apply_gradients(zip(grads_g, self.generator.trainable_variables))

        # update metrics and return
        self.d_loss_metric.update_state(d_loss)
        self.g_loss_metric.update_state(g_loss)
        return {"d_loss": self.d_loss_metric.result(),
                "g_loss": self.g_loss_metric.result()}
