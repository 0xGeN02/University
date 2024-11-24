# camara.py

import numpy as np

MIN_PITCH = -90  # Ángulo mínimo permitido para la inclinación (pitch) de la cámara
MAX_PITCH = 90   # Ángulo máximo permitido para la inclinación (pitch) de la cámara

class Camara:
    """Clase que representa una cámara en un entorno 3D.

    La cámara permite controlar su orientación en los 3 ejes (pitch, yaw y roll),
    así como su distancia (radio) respecto al punto de observación en el espacio.
    """

    def __init__(self, pitch=0, yaw=0, roll=0, radio=10.0):
        """Inicializa una instancia de la clase Camara con valores predeterminados.

        Args:
            pitch (float): Ángulo inicial de inclinación de la cámara.
            yaw (float): Ángulo inicial de rotación horizontal de la cámara.
            roll (float): Ángulo inicial de rotación lateral de la cámara.
            radio (float): Distancia inicial de la cámara respecto al punto de origen.
        """
        # Almacena los valores iniciales para poder reiniciarlos si es necesario
        self.pitch_inicial = pitch
        self.yaw_inicial = yaw
        self.roll_inicial = roll
        self.radio_inicial = radio

        # Asigna los valores actuales de pitch, yaw, roll y radio
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        self.radio = radio

        # Establece la posición inicial de la cámara en el espacio 3D
        self.cam_x, self.cam_y, self.cam_z = 0, 0, radio

    def actualizar_camara(self):
        """Actualiza la posición de la cámara en el espacio en función de pitch, yaw y radio.

        Calcula las coordenadas de la cámara en el espacio 3D usando trigonometría,
        basándose en los ángulos actuales y el radio de distancia.
        """
        self.cam_x = self.radio * np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        self.cam_y = self.radio * np.sin(np.radians(self.pitch))
        self.cam_z = self.radio * np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))

    def obtener_posicion(self):
        """Devuelve la posición actual de la cámara.

        Returns:
            tuple: Coordenadas (cam_x, cam_y, cam_z) que representan la posición en el espacio 3D.
        """
        return self.cam_x, self.cam_y, self.cam_z

    def ajustar_pitch(self, incremento):
        """Ajusta el ángulo de inclinación (pitch) dentro de los límites establecidos.

        Args:
            incremento (float): Valor a sumar al pitch actual, limitado entre MIN_PITCH y MAX_PITCH.
        """
        self.pitch = np.clip(self.pitch + incremento, MIN_PITCH, MAX_PITCH)

    def ajustar_yaw(self, incremento):
        """Ajusta el ángulo de rotación horizontal (yaw) sin límites específicos.

        Args:
            incremento (float): Valor a sumar al yaw actual.
        """
        self.yaw += incremento

    def ajustar_roll(self, incremento):
        """Ajusta el ángulo de rotación lateral (roll) de la cámara.

        Args:
            incremento (float): Valor a sumar al roll actual.
        """
        self.roll += incremento

    def ajustar_radio(self, incremento, min_radio, max_radio):
        """Ajusta la distancia (radio) de la cámara dentro de límites permitidos.

        Args:
            incremento (float): Valor a sumar al radio actual.
            min_radio (float): Límite mínimo permitido para el radio.
            max_radio (float): Límite máximo permitido para el radio.
        """
        self.radio = np.clip(self.radio + incremento, min_radio, max_radio)

    def reset(self):
        """Restaura la orientación y distancia de la cámara a sus valores iniciales."""
        self.pitch = self.pitch_inicial
        self.yaw = self.yaw_inicial
        self.roll = self.roll_inicial
        self.radio = self.radio_inicial
        self.actualizar_camara()

    def set_capture(self):
        """Restaura la orientación y distancia de la cámara a los valores establecidos
        para tomar capturas de pantalla."""
        self.pitch = 45
        self.yaw = 45
        self.roll = 0
        self.radio = 11
        self.actualizar_camara()
