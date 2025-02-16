"""
Este script utiliza OpenCV para capturar video en tiempo real y realizar predicciones de clasificación de moda en tiempo real.
"""

import os
import sys
import cv2
import numpy as np
import onnxruntime as ort

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import class_names, DATA_MODELS
# Cargar el modelo ONNX
session = ort.InferenceSession(f'{DATA_MODELS}/fashion_mnist_model.onnx')

# Capturar video en tiempo real
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocesar la imagen
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    input_image = resized.reshape(1, 28, 28, 1).astype('float32') / 255.0

    # Realizar predicción
    input_name = session.get_inputs()[0].name
    result = session.run(None, {input_name: input_image})
    predicted_class = np.argmax(result[0])

    # Mostrar la predicción en la imagen
    cv2.putText(frame, class_names[predicted_class], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Real-Time Fashion MNIST', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()