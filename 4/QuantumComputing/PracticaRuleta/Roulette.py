"""
Computación Cuántica y Natural
Actividad Práctica: La Ruleta Francesa - Parte 1 (Sin Trampas)
Alumno: Mateo Delgado
Descripción: Simulación de ruleta francesa con circuitos cuánticos independientes
             para croupier y jugadores, sin mecanismos de trampa.

Respuestas a las preguntas de la práctica:
- ¿Qué necesitas para representar 37 números? 6 qubits (2^6 = 64 posibilidades)
- ¿Qué hacer si el número resultante no está entre los 37? Repetir la medición
- ¿Qué necesitas para representar las apuestas? 3 qubits para tipos + 6 para números específicos
- ¿Mismo algoritmo cuántico para independencia? Sí, cada participante usa su propio circuito
"""

from pyquil import Program, get_qc
from pyquil.gates import H, MEASURE
from pyquil.quilbase import Declare
import numpy as np

class RouletteGame:
    def __init__(self):
        # Definir los colores de la ruleta francesa (37 números: 0-36)
        self.colors = {0: 'verde'}
        reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        
        for num in reds:
            self.colors[num] = 'rojo'
        for num in blacks:
            self.colors[num] = 'negro'
    
    def _parse_result_bits(self, result, num_bits):
        """
        Helper function para parsear bits del resultado de manera compatible.
        """
        if hasattr(result, 'get_register_map'):
            bits = result.get_register_map().get('ro')[0]
        elif hasattr(result, 'readout_data'):
            bits = result.readout_data.get('ro')[0]
        else:
            bits = result[0]
        return [bits[i] for i in range(num_bits)]
    
    def generar_numero_croupier(self):
        """
        Genera un número aleatorio entre 0 y 36 usando 6 qubits.
        Respuesta: Se necesitan 6 qubits porque 2^6 = 64 > 37
        Si el resultado es mayor que 36, se repite la medición hasta obtener un número válido.
        """
        qc = get_qc('6q-qvm')
        
        while True:
            # Crear programa cuántico con 6 qubits para representar números 0-36
            p = Program()
            ro = p.declare('ro', 'BIT', 6)
            
            # Aplicar Hadamard a todos los qubits para crear superposición equiprobable
            for i in range(6):
                p += H(i)
            
            # Medir todos los qubits
            for i in range(6):
                p += MEASURE(i, ro[i])
            
            # Ejecutar el programa
            p.wrap_in_numshots_loop(1)
            result = qc.run(p)
            
            # Convertir resultado binario a decimal
            bits = self._parse_result_bits(result, 6)
            numero = sum(bits[i] * (2 ** i) for i in range(6))
            
            # Si está en el rango válido [0-36], retornar
            if numero <= 36:
                return numero
    
    def generar_apuesta_jugador(self, jugador_id):
        """
        Genera una apuesta aleatoria para un jugador.
        Respuesta: Se usan 3 qubits para determinar el tipo de apuesta (2^3 = 8 opciones)
        """
        qc = get_qc('3q-qvm')
        
        p = Program()
        ro = p.declare('ro', 'BIT', 3)
        
        # Aplicar Hadamard para crear superposición
        for i in range(3):
            p += H(i)
        
        # Medir
        for i in range(3):
            p += MEASURE(i, ro[i])
        
        p.wrap_in_numshots_loop(1)
        result = qc.run(p)
        
        # Convertir a número
        bits = self._parse_result_bits(result, 3)
        valor = bits[0] + bits[1] * 2 + bits[2] * 4
        
        # Determinar tipo de apuesta basado en el valor (0-7)
        if valor == 0:
            # Apostar a número específico (0-36)
            numero_apostado = self.generar_numero_especifico()
            return ('numero', numero_apostado)
        elif valor == 1 or valor == 2:
            # Apostar a par o impar
            apuesta = 'par' if bits[0] == 0 else 'impar'
            return ('paridad', apuesta)
        elif valor == 3 or valor == 4:
            # Apostar a manque (1-18) o passe (19-36)
            apuesta = 'manque' if bits[0] == 0 else 'passe'
            return ('rango', apuesta)
        else:
            # Apostar a color (rojo o negro)
            apuesta = 'rojo' if bits[0] == 0 else 'negro'
            return ('color', apuesta)
    
    def generar_numero_especifico(self):
        """
        Genera un número específico entre 0 y 36 para apostar.
        Usa el mismo método que el croupier (6 qubits).
        """
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
    
    def verificar_apuesta(self, numero_croupier, tipo_apuesta, valor_apuesta):
        """
        Verifica si la apuesta del jugador coincide con el número del croupier.
        """
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
        """
        Ejecuta una ronda completa del juego.
        Nota: El croupier y los jugadores son INDEPENDIENTES - cada uno usa su propio
        circuito cuántico y nada que haga uno afecta a los demás.
        """
        print(f"\n{'='*60}")
        print(f"RONDA {ronda}")
        print(f"{'='*60}")
        
        # Generar número del croupier (circuito independiente)
        numero_croupier = self.generar_numero_croupier()
        color_croupier = self.colors[numero_croupier]
        
        print(f"\nCroupier lanza la ruleta...")
        
        # Generar apuestas de los jugadores (circuitos independientes)
        apuesta_j1 = self.generar_apuesta_jugador(1)
        apuesta_j2 = self.generar_apuesta_jugador(2)
        
        print(f"Jugador 1 apuesta: {self.formatear_apuesta(apuesta_j1)}")
        print(f"Jugador 2 apuesta: {self.formatear_apuesta(apuesta_j2)}")
        
        # Revelar resultado
        print(f"\nResultado: {numero_croupier} ({color_croupier})")
        
        # Verificar apuestas
        gana_j1 = self.verificar_apuesta(numero_croupier, apuesta_j1[0], apuesta_j1[1])
        gana_j2 = self.verificar_apuesta(numero_croupier, apuesta_j2[0], apuesta_j2[1])
        
        # Actualizar monedas según las reglas
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
        
        # Mostrar estado actual de monedas
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
    print("RULETA FRANCESA - SIMULACIÓN CUÁNTICA")
    print("Alumno: Mateo Delgado")
    print("="*60)
    
    # Inicializar juego
    juego = RouletteGame()
    
    # Estado inicial según especificaciones
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
    print(f"{'='*60}")


if __name__ == "__main__":
    main()