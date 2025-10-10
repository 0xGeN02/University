"""
Computación Cuántica y Natural
Actividad Práctica: La Ruleta Francesa - Parte 2 (Con Trampas)
Alumno: Mateo Delgado
Descripción: Simulación de ruleta francesa donde el croupier hace trampas
             espiando a un jugador aleatorio y modificando su estado cuántico
"""

from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE, X
from pyquil.quilbase import Declare
import numpy as np
import random

class RouletteGameCheating:
    def __init__(self):
        # Definir los colores de la ruleta francesa
        self.colors = {0: 'verde'}
        reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        
        for num in reds:
            self.colors[num] = 'rojo'
        for num in blacks:
            self.colors[num] = 'negro'
    
    def _parse_result_bits(self, result, num_bits):
        """
        Helper function to parse result bits from QAMExecutionResult or ndarray.
        Updated to use `get_register_map()` to address deprecation warnings.
        """
        if hasattr(result, 'get_register_map'):  # QAMExecutionResult
            bits = result.get_register_map().get('ro')[0]
        else:  # Assume ndarray
            bits = result[0]
        return [bits[i] for i in range(num_bits)]

    def generar_numero_croupier(self):
        """Genera un número aleatorio entre 0 y 36 usando 6 qubits"""
        qc = get_qc('6q-qvm')

        while True:
            p = Program()
            ro = p.declare('ro', 'BIT', 6)

            for i in range(6):
                p += H(i)

            for i in range(6):
                p += MEASURE(i, ro[i])

            p.wrap_in_numshots_loop(1)
            result = qc.run(p)

            bits = self._parse_result_bits(result, 6)
            numero = sum(bits[i] * (2 ** i) for i in range(6))

            if numero <= 36:
                return numero, bits

    def generar_apuesta_jugador(self, jugador_id):
        """Genera una apuesta aleatoria para un jugador usando circuito cuántico"""
        qc = get_qc('3q-qvm')

        p = Program()
        ro = p.declare('ro', 'BIT', 3)

        for i in range(3):
            p += H(i)

        for i in range(3):
            p += MEASURE(i, ro[i])

        p.wrap_in_numshots_loop(1)
        result = qc.run(p)

        bits = self._parse_result_bits(result, 3)
        valor = bits[0] + bits[1] * 2 + bits[2] * 4

        if valor == 0:
            numero_apostado = self.generar_numero_especifico()
            return ('numero', numero_apostado), bits
        elif valor == 1 or valor == 2:
            apuesta = 'par' if bits[0] == 0 else 'impar'
            return ('paridad', apuesta), bits
        elif valor == 3 or valor == 4:
            apuesta = 'manque' if bits[0] == 0 else 'passe'
            return ('rango', apuesta), bits
        else:
            apuesta = 'rojo' if bits[0] == 0 else 'negro'
            return ('color', apuesta), bits

    def generar_numero_especifico(self):
        """Genera un número específico entre 0 y 36 para apostar"""
        qc = get_qc('6q-qvm')

        while True:
            p = Program()
            ro = p.declare('ro', 'BIT', 6)

            for i in range(6):
                p += H(i)

            for i in range(6):
                p += MEASURE(i, ro[i])

            p.wrap_in_numshots_loop(1)
            result = qc.run(p)

            bits = self._parse_result_bits(result, 6)
            numero = sum(bits[i] * (2 ** i) for i in range(6))

            if numero <= 36:
                return numero

    def hacer_trampa(self, apuesta_espiada, numero_croupier, estado_qubits):
        """
        El croupier hace trampa: si el número coincide con la apuesta del jugador espiado,
        modifica aleatoriamente uno de sus qubits para intentar cambiar el resultado.
        """
        tipo_apuesta, valor_apuesta = apuesta_espiada

        # Verificar si hay coincidencia
        coincide = self.verificar_apuesta(numero_croupier, tipo_apuesta, valor_apuesta)

        if coincide:
            # Elegir un qubit aleatorio para modificar (0-5 para los 6 qubits del croupier)
            qubit_a_cambiar = random.randint(0, 5)

            # Crear un nuevo circuito que modifique ese qubit
            qc = get_qc('6q-qvm')
            p = Program()
            ro = p.declare('ro', 'BIT', 6)

            # Reconstruir el estado y aplicar X gate al qubit seleccionado
            for i in range(6):
                if estado_qubits[i] == 1:
                    p += X(i)

            # Aplicar la trampa: voltear el qubit seleccionado
            p += X(qubit_a_cambiar)

            # Medir todos los qubits
            for i in range(6):
                p += MEASURE(i, ro[i])

            p.wrap_in_numshots_loop(1)
            result = qc.run(p)

            bits = self._parse_result_bits(result, 6)
            nuevo_numero = sum(bits[i] * (2 ** i) for i in range(6))

            # Si el nuevo número está fuera de rango, intentar con otro qubit
            intentos = 0
            while nuevo_numero > 36 and intentos < 6:
                qubit_a_cambiar = random.randint(0, 5)
                p = Program()
                ro = p.declare('ro', 'BIT', 6)

                for i in range(6):
                    if estado_qubits[i] == 1:
                        p += X(i)

                p += X(qubit_a_cambiar)

                for i in range(6):
                    p += MEASURE(i, ro[i])

                p.wrap_in_numshots_loop(1)
                result = qc.run(p)
                bits = self._parse_result_bits(result, 6)
                nuevo_numero = sum(bits[i] * (2 ** i) for i in range(6))
                intentos += 1

            if nuevo_numero <= 36:
                return nuevo_numero, True, qubit_a_cambiar
            else:
                return numero_croupier, False, None

        return numero_croupier, False, None
    
    def verificar_apuesta(self, numero_croupier, tipo_apuesta, valor_apuesta):
        """Verifica si la apuesta del jugador coincide con el número del croupier"""
        if tipo_apuesta == 'numero':
            return numero_croupier == valor_apuesta
        
        elif tipo_apuesta == 'paridad':
            if numero_croupier == 0:
                return False
            es_par = numero_croupier % 2 == 0
            return (valor_apuesta == 'par' and es_par) or (valor_apuesta == 'impar' and not es_par)
        
        elif tipo_apuesta == 'rango':
            if numero_croupier == 0:
                return False
            return (valor_apuesta == 'manque' and 1 <= numero_croupier <= 18) or \
                   (valor_apuesta == 'passe' and 19 <= numero_croupier <= 36)
        
        elif tipo_apuesta == 'color':
            return self.colors[numero_croupier] == valor_apuesta
        
        return False
    
    def jugar_ronda(self, ronda, monedas_j1, monedas_j2, monedas_croupier):
        """Ejecuta una ronda completa del juego con trampas del croupier"""
        print(f"\n{'='*60}")
        print(f"RONDA {ronda}")
        print(f"{'='*60}")
        
        # Generar número inicial del croupier
        numero_croupier, estado_qubits_croupier = self.generar_numero_croupier()
        
        print(f"\nCroupier prepara la ruleta...")
        
        # Generar apuestas de los jugadores
        apuesta_j1, estado_j1 = self.generar_apuesta_jugador(1)
        apuesta_j2, estado_j2 = self.generar_apuesta_jugador(2)
        
        print(f"Jugador 1 apuesta: {self.formatear_apuesta(apuesta_j1)}")
        print(f"Jugador 2 apuesta: {self.formatear_apuesta(apuesta_j2)}")
        
        # El croupier hace trampa: espía a un jugador aleatorio
        jugador_espiado = random.choice([1, 2])
        apuesta_espiada = apuesta_j1 if jugador_espiado == 1 else apuesta_j2
        
        print(f"\n[SISTEMA] El croupier espía al Jugador {jugador_espiado}...")
        
        # Hacer trampa si es necesario
        numero_final, hizo_trampa, qubit_modificado = self.hacer_trampa(
            apuesta_espiada, numero_croupier, estado_qubits_croupier
        )
        
        if hizo_trampa:
            print(f"[TRAMPA DETECTADA] Qubit {qubit_modificado} modificado")
            print(f"   Número original: {numero_croupier} -> Número modificado: {numero_final}")
        else:
            print(f"   No se requirió modificación del estado cuántico")
        
        color_final = self.colors[numero_final]
        
        # Revelar resultado
        print(f"\nResultado final: {numero_final} ({color_final})")
        
        # Verificar apuestas
        gana_j1 = self.verificar_apuesta(numero_final, apuesta_j1[0], apuesta_j1[1])
        gana_j2 = self.verificar_apuesta(numero_final, apuesta_j2[0], apuesta_j2[1])
        
        # Actualizar monedas
        if gana_j1:
            monedas_j1 += 1
            monedas_croupier -= 1
            print("Jugador 1 GANA (+1 moneda)")
        else:
            monedas_j1 -= 1
            monedas_croupier += 1
            print("Jugador 1 PIERDE (-1 moneda)")
        
        if gana_j2:
            monedas_j2 += 1
            monedas_croupier -= 1
            print("Jugador 2 GANA (+1 moneda)")
        else:
            monedas_j2 -= 1
            monedas_croupier += 1
            print("Jugador 2 PIERDE (-1 moneda)")
        
        # Mostrar estado actual
        print(f"\nEstado de monedas:")
        print(f"   Jugador 1: {monedas_j1} monedas")
        print(f"   Jugador 2: {monedas_j2} monedas")
        print(f"   Croupier:  {monedas_croupier} monedas")
        
        return monedas_j1, monedas_j2, monedas_croupier
    
    def formatear_apuesta(self, apuesta):
        """Formatea la apuesta para mostrarla de forma legible"""
        tipo, valor = apuesta
        if tipo == 'numero':
            return f"Número {valor}"
        elif tipo == 'paridad':
            return f"Números {'pares' if valor == 'par' else 'impares'}"
        elif tipo == 'rango':
            return f"{'Manque (1-18)' if valor == 'manque' else 'Passe (19-36)'}"
        elif tipo == 'color':
            return f"Color {valor}"
        return str(apuesta)


def main():
    print("="*60)
    print("RULETA FRANCESA - SIMULACIÓN CUÁNTICA (CON TRAMPAS)")
    print("Alumno: Mateo Delgado")
    print("="*60)
    print("\nNOTA: En esta versión el croupier hace trampas")
    print("      Espía a un jugador aleatorio y puede modificar el resultado")
    
    # Inicializar juego
    juego = RouletteGameCheating()
    
    # Estado inicial
    monedas_j1 = 10
    monedas_j2 = 10
    monedas_croupier = 20
    num_rondas = 10
    
    print(f"\nMonedas iniciales:")
    print(f"   Jugador 1: {monedas_j1} monedas")
    print(f"   Jugador 2: {monedas_j2} monedas")
    print(f"   Croupier:  {monedas_croupier} monedas")
    print(f"\nNúmero de rondas: {num_rondas}")
    
    # Jugar rondas
    for ronda in range(1, num_rondas + 1):
        monedas_j1, monedas_j2, monedas_croupier = juego.jugar_ronda(
            ronda, monedas_j1, monedas_j2, monedas_croupier
        )
    
    # Resultado final
    print(f"\n{'='*60}")
    print("RESULTADO FINAL")
    print(f"{'='*60}")
    print(f"Jugador 1: {monedas_j1} monedas (Cambio: {monedas_j1 - 10:+d})")
    print(f"Jugador 2: {monedas_j2} monedas (Cambio: {monedas_j2 - 10:+d})")
    print(f"Croupier:  {monedas_croupier} monedas (Cambio: {monedas_croupier - 20:+d})")
    print(f"\nNota: Las trampas del croupier afectaron los resultados")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()