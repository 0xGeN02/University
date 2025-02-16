"""
Este script convierte el modelo entrenado en un archivo ONNX.
"""

import os
import sys
import tensorflow as tf
import onnx
from tensorflow.keras.models import load_model
import tf2onnx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import DATA_MODELS

# Cargar el modelo entrenado
model = load_model(f'{DATA_MODELS}/fashion_mnist_model.h5')

# Asignar manualmente output_names
if not hasattr(model, 'output_names'):
    model.output_names = [model.layers[-1].name]

# Convertir a ONNX
spec = (tf.TensorSpec((None, 28, 28, 1), tf.float32, name="input"),)
output_path = f'{DATA_MODELS}/fashion_mnist_model.onnx'
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=13)
onnx.save_model(model_proto, output_path)
