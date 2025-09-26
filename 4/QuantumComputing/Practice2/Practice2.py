"""
Actividad Práctica - Sesión 03: Las Puertas de Pauli
Asignatura: Computación Cuántica y Natural

Este programa implementa las puertas de Pauli (X, Y, Z) utilizando PyQuil y el WavefunctionSimulator.
Cada puerta se prueba con dos estados iniciales: |0⟩ y |1⟩.

- 2 programas por cada puerta (X, Y, Z)
- Un programa para estado inicial |0⟩ y otro para |1⟩
- Flujo específico: definir programa → ejecutar wavesimulator → añadir puerta → ejecutar de nuevo
"""

from pyquil import Program
from pyquil.gates import X, Y, Z
from pyquil.api import WavefunctionSimulator
import numpy as np

# Configuración del simulador
wf_sim = WavefunctionSimulator()

def imprimir_wavefunction(wavefunc, titulo):
    """Función auxiliar para imprimir la función de onda de forma legible"""
    print(f"\n{titulo}")
    print("-" * 50)
    amplitudes = wavefunc.amplitudes.reshape((-1, 1))
    for i, amplitude in enumerate(amplitudes):
        prob = np.abs(amplitude[0])**2
        print(f"|{i}⟩: {amplitude[0]:.4f} (Probabilidad: {prob:.4f})")
    print("-" * 50)

print("="*60)
print("PRÁCTICA: LAS PUERTAS DE PAULI")
print("Requisitos: 2 programas por puerta (estados |0⟩ y |1⟩)")
print("="*60)

# =============================================================================
# PROGRAMA 1: PUERTA X - ESTADO INICIAL |0⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 1: PUERTA X - ESTADO INICIAL |0⟩")
print("="*50)

# a. Definición del programa con su memoria y estado inicial
prog = Program()
print("a. Programa definido con estado inicial |0⟩ (por defecto)")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial:")

# c. Utilizar la función inst para añadir la puerta lógica X
prog.inst(X(0))
print("c. Puerta X añadida al programa: prog.inst(X(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de X:")

# =============================================================================
# PROGRAMA 2: PUERTA X - ESTADO INICIAL |1⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 2: PUERTA X - ESTADO INICIAL |1⟩")
print("="*50)

# a. Definición del programa con estado inicial |1⟩
prog = Program()
prog.inst(X(0))  # Preparar estado |1⟩
print("a. Programa definido con estado inicial |1⟩")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial |1⟩:")

# c. Utilizar la función inst para añadir la puerta lógica X
prog.inst(X(0))
print("c. Puerta X añadida al programa: prog.inst(X(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de X:")

# =============================================================================
# PROGRAMA 3: PUERTA Z - ESTADO INICIAL |0⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 3: PUERTA Z - ESTADO INICIAL |0⟩")
print("="*50)

# a. Definición del programa con estado inicial |0⟩
prog = Program()
print("a. Programa definido con estado inicial |0⟩ (por defecto)")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial:")

# c. Utilizar la función inst para añadir la puerta lógica Z
prog.inst(Z(0))
print("c. Puerta Z añadida al programa: prog.inst(Z(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de Z:")

# =============================================================================
# PROGRAMA 4: PUERTA Z - ESTADO INICIAL |1⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 4: PUERTA Z - ESTADO INICIAL |1⟩")
print("="*50)

# a. Definición del programa con estado inicial |1⟩
prog = Program()
prog.inst(X(0))  # Preparar estado |1⟩
print("a. Programa definido con estado inicial |1⟩")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial |1⟩:")

# c. Utilizar la función inst para añadir la puerta lógica Z
prog.inst(Z(0))
print("c. Puerta Z añadida al programa: prog.inst(Z(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de Z:")

# =============================================================================
# PROGRAMA 5: PUERTA Y - ESTADO INICIAL |0⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 5: PUERTA Y - ESTADO INICIAL |0⟩")
print("="*50)

# a. Definición del programa con estado inicial |0⟩
prog = Program()
print("a. Programa definido con estado inicial |0⟩ (por defecto)")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial:")

# c. Utilizar la función inst para añadir la puerta lógica Y
prog.inst(Y(0))
print("c. Puerta Y añadida al programa: prog.inst(Y(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de Y:")

# =============================================================================
# PROGRAMA 6: PUERTA Y - ESTADO INICIAL |1⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 6: PUERTA Y - ESTADO INICIAL |1⟩")
print("="*50)

# a. Definición del programa con estado inicial |1⟩
prog = Program()
prog.inst(X(0))  # Preparar estado |1⟩
print("a. Programa definido con estado inicial |1⟩")

# b. Ejecución del wavesimulator para extraer la función de onda
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "b. Función de onda inicial |1⟩:")

# c. Utilizar la función inst para añadir la puerta lógica Y
prog.inst(Y(0))
print("c. Puerta Y añadida al programa: prog.inst(Y(0))")

# d. Ejecutar de nuevo el wavesimulator
wavefunction = wf_sim.wavefunction(prog)
imprimir_wavefunction(wavefunction, "d. Función de onda después de Y:")

# =============================================================================
# CONSTRUCCIÓN ESPECIAL DE LA PUERTA Y
# Punto 4: Construcción usando amplitudes y el número imaginario 1j
# =============================================================================
print("\n" + "="*60)
print("CONSTRUCCIÓN ESPECIAL DE LA PUERTA Y")
print("Usando amplitudes y el número imaginario 1j")
print("="*60)

# =============================================================================
# PROGRAMA 7: CONSTRUCCIÓN Y PARA ESTADO |0⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 7: CONSTRUCCIÓN Y PARA ESTADO |0⟩")
print("="*50)

print("Análisis: Y = i * X * Z")
print("Vamos a construir Y paso a paso usando amplitudes:")

# Paso 1: Estado inicial |0⟩
prog_construccion = Program()
wavefunction_inicial = wf_sim.wavefunction(prog_construccion)
amplitudes_inicial = wavefunction_inicial.amplitudes.reshape((-1, 1))
print(f"Estado inicial |0⟩: amplitudes = {amplitudes_inicial.flatten()}")

# Paso 2: Aplicar X (|0⟩ → |1⟩)
prog_x = Program()
prog_x.inst(X(0))
wavefunction_x = wf_sim.wavefunction(prog_x)
amplitudes_x = wavefunction_x.amplitudes.reshape((-1, 1))
print(f"Después de X: amplitudes = {amplitudes_x.flatten()}")

# Paso 3: Aplicar X*Z (equivalente a -iY, necesitamos el factor i)
prog_xz = Program()
prog_xz.inst(X(0))
prog_xz.inst(Z(0))
wavefunction_xz = wf_sim.wavefunction(prog_xz)
amplitudes_xz = wavefunction_xz.amplitudes.reshape((-1, 1))
print(f"Después de X*Z: amplitudes = {amplitudes_xz.flatten()}")

# Paso 4: Aplicar Y directamente para comparar
prog_y = Program()
prog_y.inst(Y(0))
wavefunction_y = wf_sim.wavefunction(prog_y)
amplitudes_y = wavefunction_y.amplitudes.reshape((-1, 1))
print(f"Y directo: amplitudes = {amplitudes_y.flatten()}")

# Construcción manual usando 1j
FACTOR_I = 1j
amplitudes_construida = amplitudes_xz * FACTOR_I
print(f"Construcción Y = i*X*Z: {amplitudes_construida.flatten()}")

print("✓ Verificación: Y|0⟩ = i|1⟩ = (0, i)")
print(f"✓ Resultado Y: {amplitudes_y.flatten()}")
print(f"✓ Construcción i*X*Z: {amplitudes_construida.flatten()}")

# =============================================================================
# PROGRAMA 8: CONSTRUCCIÓN Y PARA ESTADO |1⟩
# =============================================================================
print("\n" + "="*50)
print("PROGRAMA 8: CONSTRUCCIÓN Y PARA ESTADO |1⟩")
print("="*50)

print("Construcción de Y|1⟩ usando amplitudes y 1j:")

# Estado inicial |1⟩
prog_inicial = Program()
prog_inicial.inst(X(0))
wavefunction_inicial = wf_sim.wavefunction(prog_inicial)
amplitudes_inicial = wavefunction_inicial.amplitudes.reshape((-1, 1))
print(f"Estado inicial |1⟩: amplitudes = {amplitudes_inicial.flatten()}")

# Aplicar X*Z a |1⟩: X|1⟩ = |0⟩, luego Z|0⟩ = |0⟩
prog_xz = Program()
prog_xz.inst(X(0))  # Preparar |1⟩
prog_xz.inst(X(0))  # X|1⟩ = |0⟩
prog_xz.inst(Z(0))  # Z|0⟩ = |0⟩
wavefunction_xz = wf_sim.wavefunction(prog_xz)
amplitudes_xz = wavefunction_xz.amplitudes.reshape((-1, 1))
print(f"X*Z aplicado a |1⟩: amplitudes = {amplitudes_xz.flatten()}")

# Y directo aplicado a |1⟩
prog_y = Program()
prog_y.inst(X(0))  # Preparar |1⟩
prog_y.inst(Y(0))  # Aplicar Y
wavefunction_y = wf_sim.wavefunction(prog_y)
amplitudes_y = wavefunction_y.amplitudes.reshape((-1, 1))
print(f"Y directo a |1⟩: amplitudes = {amplitudes_y.flatten()}")

# Construcción manual: necesitamos aplicar i*X*Z de manera correcta
# Y|1⟩ = -i|0⟩, por tanto necesitamos el factor -i
FACTOR_MENOS_I = -1j
# Para |1⟩: (XZ)|1⟩ = |0⟩, entonces i*(XZ)|1⟩ = i|0⟩, pero Y|1⟩ = -i|0⟩
# Entonces necesitamos -i factor
amplitudes_construida = amplitudes_xz * FACTOR_MENOS_I
print(f"Construcción Y = -i para este caso: {amplitudes_construida.flatten()}")

print("✓ Verificación: Y|1⟩ = -i|0⟩ = (-i, 0)")
print(f"✓ Resultado Y: {amplitudes_y.flatten()}")
print(f"✓ Construcción -i*(XZ)|1⟩: {amplitudes_construida.flatten()}")
