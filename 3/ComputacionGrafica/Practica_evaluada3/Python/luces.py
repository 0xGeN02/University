# luces.py

from OpenGL.GL import *

def configurar_luces():
    """Configura las luces de la escena en OpenGL."""
    POSICION_LUZ1 = [5.0, 5.0, 5.0, 1.0]
    POSICION_LUZ2 = [-5.0, 5.0, -5.0, 1.0]
    LUZ_AMBIENTE = [0.3, 0.3, 0.3, 1.0]
    LUZ_DIFUSA = [0.8, 0.8, 0.8, 1.0]
    LUZ_ESPECULAR = [0.5, 0.5, 0.5, 1.0]
    COEFICIENTE_ESPECULAR = [0.5, 0.5, 0.5, 1.0]
    EXPONENTE_BRILLO = 20.0

    # Configuración de la luz 1 (GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LUZ_AMBIENTE)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LUZ_DIFUSA)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LUZ_ESPECULAR)
    glLightfv(GL_LIGHT0, GL_POSITION, POSICION_LUZ1)

    # Configuración de la luz 2 (GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, LUZ_AMBIENTE)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, LUZ_DIFUSA)
    glLightfv(GL_LIGHT1, GL_SPECULAR, LUZ_ESPECULAR)
    glLightfv(GL_LIGHT1, GL_POSITION, POSICION_LUZ2)

    # Configura la componente especular del material
    glMaterialfv(GL_FRONT, GL_SPECULAR, COEFICIENTE_ESPECULAR)
    # Configura el exponente de brillo del material
    glMaterialf(GL_FRONT, GL_SHININESS, EXPONENTE_BRILLO)

    # Establece el color de fondo para reducir el contraste con el objeto
    glClearColor(0.1, 0.1, 0.1, 1.0)
