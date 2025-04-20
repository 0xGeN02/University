# import the necessary packages
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import ReLU
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Reshape

def get_generator(weight_init, latent_dim, channels):
	# create a Keras Sequential model 
	model = Sequential(name="generator")

	# prepare for reshape: FC => BN => RN layers,
	# note: input shape defined in the 1st Dense layer  
	model.add(Dense(7 * 7 * 256, input_dim=latent_dim))
	model.add(BatchNormalization())
	model.add(ReLU())

	# 1D => 3D: reshape the output of the previous layer 
	model.add(Reshape((7, 7, 256)))

	# upsample to 14x14: apply a transposed CONV => BN => RELU
	model.add(Conv2DTranspose(128, (5, 5), strides=(2, 2),
		padding="same", kernel_initializer=weight_init))
	model.add(BatchNormalization())
	model.add((ReLU()))

	# upsample to 28x28: apply a transposed CONV => BN => RELU
	model.add(Conv2DTranspose(64, (5, 5), strides=(2, 2),
		padding="same", kernel_initializer=weight_init))
	model.add(BatchNormalization())
	model.add((ReLU()))

	# final layer: Conv2D with tanh activation
	model.add(Conv2D(channels, (5, 5), padding="same",
		activation="tanh"))

	# return the generator model
	return model

def get_discriminator(width, height, depth, alpha=0.2):
	# create a Keras Sequential model
	model = Sequential(name="discriminator")
	input_shape = (height, width, depth)

	# first set of CONV => BN => leaky ReLU layers
	model.add(Conv2D(64, (5, 5), strides=(2, 2), padding="same", 
		input_shape=input_shape))
	model.add(BatchNormalization())
	model.add(LeakyReLU(alpha=alpha))

	# second set of CONV => BN => leacy ReLU layers
	model.add(Conv2D(128, (5, 5), strides=(2, 2), padding="same"))
	model.add(BatchNormalization())
	model.add(LeakyReLU(alpha=alpha))

	# flatten and apply dropout
	model.add(Flatten())
	model.add(Dropout(0.3))

	# sigmoid in the last layer outputs a single value for
	# binary classification
	model.add(Dense(1, activation="sigmoid"))

	# return the discriminator model
	return model