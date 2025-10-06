"""
Ruleta Francesa - Versión con trampas
Computación Cuántica y Natural - Sesión 05

En esta versión, el croupier hace trampas:
- Conoce el resultado de un jugador aleatorio
- Si coincide con su número, modifica un qubit aleatorio
"""

import random
from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE, X

# Configuración de la ruleta francesa
NUMEROS_ROJOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
NUMEROS_NEGROS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def obtener_color(numero):
    """Devuelve el color del número en la ruleta"""
    if numero == 0:
        return "verde"
    if numero in NUMEROS_ROJOS:
        return "rojo"
    return "negro"

def generar_numero_croupier_con_trampa(debe_hacer_trampa=False):
    """
    Genera un número aleatorio entre 0 y 36 usando 6 qubits.
    Si debe_hacer_trampa es True, modifica un qubit aleatorio.
    """
    qc = get_qc('6q-qvm')

    while True:
        p = Program()
        ro = p.declare('ro', 'BIT', 6)

        # Aplicar Hadamard a todos los qubits para crear superposición
        for i in range(6):
            p += H(i)

        # Si debe hacer trampa, modificar un qubit aleatorio
        if debe_hacer_trampa:
            qubit_trampa = random.randint(0, 5)
            p += X(qubit_trampa)
            print(f"  [TRAMPA] Croupier modifica el qubit {qubit_trampa}")

        # Medir todos los qubits
        for i in range(6):
            p += MEASURE(i, ro[i])

        p.wrap_in_numshots_loop(1)
        resultado = qc.run(p)

        # Convertir el resultado binario a decimal
        numero = sum(int(resultado[0][i]) * (2**i) for i in range(6))
        # Solo aceptar números válidos (0-36)
        if numero <= 36:
            return numero

def generar_apuesta_jugador(tipo_apuesta):
    """
    Genera una apuesta aleatoria según el tipo especificado.
    
    Tipos de apuesta:
    - 'numero': apuesta a un número específico (0-36) - necesita 6 qubits
    - 'paridad': par o impar - necesita 1 qubit
    - 'mitad': manque (1-18) o passe (19-36) - necesita 1 qubit
    - 'color': rojo o negro - necesita 1 qubit
    """
    qc = get_qc('6q-qvm')

    if tipo_apuesta == 'numero':
        while True:
            p = Program()
            ro = p.declare('ro', 'BIT', 6)

            for i in range(6):
                p += H(i)

            for i in range(6):
                p += MEASURE(i, ro[i])

            p.wrap_in_numshots_loop(1)
            resultado = qc.run(p)
            numero = sum(int(resultado[0][i]) * (2**i) for i in range(6))

            if numero <= 36:
                return numero

    elif tipo_apuesta in ['paridad', 'mitad', 'color']:
        p = Program()
        ro = p.declare('ro', 'BIT', 1)

        p += H(0)
        p += MEASURE(0, ro[0])

        p.wrap_in_numshots_loop(1)
        resultado = qc.run(p)

        if tipo_apuesta == 'paridad':
            return 'par' if resultado[0][0] == 0 else 'impar'
        if tipo_apuesta == 'mitad':
            return 'manque' if resultado[0][0] == 0 else 'passe'
        if tipo_apuesta == 'color':
            return 'rojo' if resultado[0][0] == 0 else 'negro'
        return TypeError
    return TypeError

def verificar_apuesta(numero_croupier, tipo_apuesta, apuesta):
    """Verifica si una apuesta gana según el número del croupier"""
    if tipo_apuesta == 'numero':
        return numero_croupier == apuesta

    if tipo_apuesta == 'paridad' & numero_croupier != 0:
        es_par = numero_croupier % 2 == 0
        return (apuesta == 'par' and es_par) or (apuesta == 'impar' and not es_par)

    if tipo_apuesta == 'mitad' & numero_croupier != 0:
        es_manque = 1 <= numero_croupier <= 18
        return (apuesta == 'manque' and es_manque) or (apuesta == 'passe' and not es_manque)

    if tipo_apuesta == 'color':
        color = obtener_color(numero_croupier)
        return apuesta == color

    return False

def jugador_coincide_con_numero(numero_croupier, tipo_apuesta, apuesta):
    """
    Verifica si la apuesta del jugador coincide con el número del croupier.
    Usado para determinar si el croupier debe hacer trampa.
    """
    return verificar_apuesta(numero_croupier, tipo_apuesta, apuesta)

def jugar_ronda(jugadores_config, ronda):
    """Juega una ronda completa del juego con posibilidad de trampa"""
    print(f"\n{'='*60}")
    print(f"RONDA {ronda}")
    print(f"{'='*60}")

    # Primera generación del número del croupier (sin trampa)
    numero_croupier_inicial = generar_numero_croupier_con_trampa(debe_hacer_trampa=False)

    # Cada jugador genera su apuesta
    apuestas_jugadores = []
    for i, config in enumerate(jugadores_config, 1):
        tipo = config['tipo']
        apuesta = generar_apuesta_jugador(tipo)
        apuestas_jugadores.append((tipo, apuesta))
        print(f"\nJugador {i}:")
        print(f"  Tipo de apuesta: {tipo}")
        print(f"  Apuesta: {apuesta}")

    # El croupier "espía" a un jugador aleatorio
    jugador_espiado = random.randint(0, len(jugadores_config) - 1)
    tipo_espiado, apuesta_espiada = apuestas_jugadores[jugador_espiado]

    print(f"\n[CROUPIER] Espiando al Jugador {jugador_espiado + 1}...")

    # Verificar si el resultado inicial del croupier coincide con el jugador espiado
    coincide = jugador_coincide_con_numero(numero_croupier_inicial, tipo_espiado, apuesta_espiada)

    if coincide:
        print("[CROUPIER] ¡El jugador espiado ganaría! Haciendo trampa...")
        numero_croupier = generar_numero_croupier_con_trampa(debe_hacer_trampa=True)
    else:
        print("[CROUPIER] El jugador espiado perdería. No hay necesidad de trampa.")
        numero_croupier = numero_croupier_inicial

    color_croupier = obtener_color(numero_croupier)
    print("\nCroupier gira la ruleta...")
    print(f"¡Número ganador: {numero_croupier} ({color_croupier})!")

    # Verificar resultados
    resultados = []
    for i, (tipo, apuesta) in enumerate(apuestas_jugadores, 1):
        gana = verificar_apuesta(numero_croupier, tipo, apuesta)
        print(f"\nJugador {i}:")
        print(f"  Resultado: {'¡GANA!' if gana else 'Pierde'}")
        resultados.append(gana)

    return numero_croupier, resultados

def main():
    """Función principal del juego"""
    print("="*60)
    print("RULETA FRANCESA - VERSIÓN CON TRAMPAS")
    print("="*60)
    print("El croupier espía a un jugador aleatorio en cada ronda")
    print("y hace trampa si ese jugador ganaría")
    print("="*60)

    # Configuración del juego
    num_rondas = 10

    # Configuración de jugadores
    jugadores_config = [
        {'tipo': 'numero'},    # Jugador 1 apuesta a números específicos
        {'tipo': 'color'}      # Jugador 2 apuesta a colores
    ]

    # Monedas iniciales
    monedas_jugador1 = 10
    monedas_jugador2 = 10
    monedas_croupier = 20

    print(f"\nNúmero de rondas: {num_rondas}")
    print("Monedas iniciales:")
    print(f"  Jugador 1: {monedas_jugador1}")
    print(f"  Jugador 2: {monedas_jugador2}")
    print(f"  Croupier: {monedas_croupier}")

    # Jugar todas las rondas
    for ronda in range(1, num_rondas + 1):
        _, resultados = jugar_ronda(jugadores_config, ronda)

        # Actualizar monedas
        if resultados[0]:  # Jugador 1 gana
            monedas_jugador1 += 1
            monedas_croupier -= 1
        else:
            monedas_jugador1 -= 1
            monedas_croupier += 1

        if resultados[1]:  # Jugador 2 gana
            monedas_jugador2 += 1
            monedas_croupier -= 1
        else:
            monedas_jugador2 -= 1
            monedas_croupier += 1

        # Mostrar estado de monedas
        print(f"\n{'·'*60}")
        print(f"Estado de monedas después de la ronda {ronda}:")
        print(f"  Jugador 1: {monedas_jugador1} monedas")
        print(f"  Jugador 2: {monedas_jugador2} monedas")
        print(f"  Croupier: {monedas_croupier} monedas")

    # Resumen final
    print(f"\n{'='*60}")
    print("RESULTADO FINAL")
    print(f"{'='*60}")
    print(f"Jugador 1: {monedas_jugador1} monedas (cambio: {monedas_jugador1 - 10:+d})")
    print(f"Jugador 2: {monedas_jugador2} monedas (cambio: {monedas_jugador2 - 10:+d})")
    print(f"Croupier: {monedas_croupier} monedas (cambio: {monedas_croupier - 20:+d})")
    print("="*60)

if __name__ == "__main__":
    main()
