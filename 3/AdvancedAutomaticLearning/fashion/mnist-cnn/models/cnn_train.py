"""
Entrenamiento de una red neuronal convolucional (CNN) para clasificar imágenes de prendas de vestir
"""

import os
import sys
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import FASHION_CSV, DATA_MODELS
from src import data_loader

# Cargar datos
images, labels = data_loader.load_data(FASHION_CSV)
labels = tf.keras.utils.to_categorical(labels, 10)

# Dividir datos en entrenamiento y prueba
train_images, test_images = images[:8000], images[8000:]
train_labels, test_labels = labels[:8000], labels[8000:]

# Definir el modelo CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Guardar el modelo en formato ONNX
model.save(f'{DATA_MODELS}/fashion_mnist_model.h5')
