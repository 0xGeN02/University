# esqueleto.py

from configuracion_esqueleto import *
from articulacion import *
from cinematica import *

def configurar_esqueleto():

    ###############################
    #            TRONCO           #
    ###############################

    # Articulación Raíz (Pelvis)
    raiz = Articulacion(
        angulo=0,
        angulo_min=-360,  # Sin límite para la articulación raíz
        angulo_max=360,
        r=[0, 0],
    )

    # Torso (articulación rígida entre los hombros)
    torso = Articulacion(
        padre=raiz,
        r=[0, 6],
    )

    ###############################
    #        BRAZO DERECHO        #
    ###############################
    # Hombro derecho
    hombro_derecho = Articulacion(
        padre=torso,
        angulo=ANGULO_INICIAL_HOMBRO_DERECHO,
        angulo_min=ANGULO_MIN_HOMBRO_DERECHO,
        angulo_max=ANGULO_MAX_HOMBRO_DERECHO,
        r=[3, 0],
    )
    
    # Codo derecho
    codo_derecho = Articulacion(
        padre=hombro_derecho,
        angulo=ANGULO_INICIAL_CODO_DERECHO,
        angulo_min=ANGULO_MIN_CODO_DERECHO,
        angulo_max=ANGULO_MAX_CODO_DERECHO,
        r=[4, 0],
    )
    
    # Muñeca derecha
    muneca_derecha = Articulacion(
        padre=codo_derecho,
        angulo=ANGULO_INICIAL_MUNECA_DERECHA,
        angulo_min=ANGULO_MIN_MUNECA_DERECHA,
        angulo_max=ANGULO_MAX_MUNECA_DERECHA,
        r=[3, 0],
    )
    
    #Mano derecha
    mano_derecha = Articulacion(
        padre=muneca_derecha,
        angulo=0,
        r=[1, 0],
    )

    ###############################
    #       BRAZO IZQUIERDO       #
    ###############################

    #Hombro izquierdo
    hombro_izquierdo = Articulacion(
        padre=torso,
        angulo=ANGULO_INICIAL_HOMBRO_IZQUIERDO,
        angulo_min=ANGULO_MIN_HOMBRO_IZQUIERDO,
        angulo_max=ANGULO_MAX_HOMBRO_IZQUIERDO,
        r=[-3, 0],
    )
    
    #Codo izquierdo
    codo_izquierdo = Articulacion(
        padre=hombro_izquierdo,
        angulo=ANGULO_INICIAL_CODO_IZQUIERDO,
        angulo_min=ANGULO_MIN_CODO_IZQUIERDO,
        angulo_max=ANGULO_MAX_CODO_IZQUIERDO,
        r=[-4, 0],
    )
    
    #Muñeca izquierda
    muneca_izquierda = Articulacion(
        padre=codo_izquierdo,
        angulo=ANGULO_INICIAL_MUNECA_IZQUIERDA,
        angulo_min=ANGULO_MIN_MUNECA_IZQUIERDA,
        angulo_max=ANGULO_MAX_MUNECA_IZQUIERDA,
        r=[-3, 0],
    )
    
    #Mano izquierda
    mano_izquierda = Articulacion(
        padre=muneca_izquierda,
        angulo=0,
        r=[-1, 0],
    )
    
    ###############################
    #        PIERNA DERECHA       #
    ###############################

    # Cadera derecha
    cadera_derecha = Articulacion(
        padre=raiz,
        angulo=ANGULO_INICIAL_CADERA_DERECHA,
        angulo_min=ANGULO_MIN_CADERA_DERECHA,
        angulo_max=ANGULO_MAX_CADERA_DERECHA,
        r=[1, 0],
    )
    
    # Rodilla derecha
    rodilla_derecha = Articulacion(
        padre=cadera_derecha,
        angulo=ANGULO_INICIAL_RODILLA_DERECHA,
        angulo_min=ANGULO_MIN_RODILLA_DERECHA,
        angulo_max=ANGULO_MAX_RODILLA_DERECHA,
        r=[5, 0],
    )
    
    # Tobillo derecho
    tobillo_derecho = Articulacion(
        padre=rodilla_derecha,
        angulo=ANGULO_INICIAL_TOBILLO_DERECHO,
        angulo_min=ANGULO_MIN_TOBILLO_DERECHO,
        angulo_max=ANGULO_MAX_TOBILLO_DERECHO,
        r=[4, 0],
    )
    
    # Pie derecho
    pie_derecho = Articulacion(
        padre=tobillo_derecho,
        angulo=0,
        r=[1, 0],
    )

    ###############################
    #       PIERNA IZQUIERDA      #
    ###############################

    #Cadera izquierda
    cadera_izquierda = Articulacion(
        padre=raiz,
        angulo=ANGULO_INICIAL_CADERA_IZQUIERDA,
        angulo_min=ANGULO_MIN_CADERA_IZQUIERDA,
        angulo_max=ANGULO_MAX_CADERA_IZQUIERDA,
        r=[-1, 0],
    )
    
    #Rodilla izquierda
    rodilla_izquierda = Articulacion(
        padre=cadera_izquierda,
        angulo=ANGULO_INICIAL_RODILLA_IZQUIERDA,
        angulo_min=ANGULO_MIN_RODILLA_IZQUIERDA,
        angulo_max=ANGULO_MAX_RODILLA_IZQUIERDA,
        r=[-5, 0],
    )
    
    #Tobillo izquierdo
    tobillo_izquierdo = Articulacion(
        padre=rodilla_izquierda,
        angulo=ANGULO_INICIAL_TOBILLO_IZQUIERDO,
        angulo_min=ANGULO_MIN_TOBILLO_IZQUIERDO,
        angulo_max=ANGULO_MAX_TOBILLO_IZQUIERDO,
        r=[-4, 0],
    )
    
    #Pie izquierdo
    pie_izquierdo = Articulacion(
        padre=tobillo_izquierdo,
        angulo=0,
        r=[-1, 0],
    )

    # Inicializar matrices de transformación
    actualizar_matrices(raiz)

    return raiz, Articulacion.articulaciones