"""
Actividad Práctica S04 - Computación Cuántica
Puertas cuánticas de fase y rotación con PyQuil
"""

from pyquil import Program
from pyquil.gates import I, X, PHASE, S, T, RX, RY, RZ
from pyquil.simulation.tools import program_unitary
from pyquil.api import WavefunctionSimulator
import numpy as np

# Inicializar el simulador de función de onda
wf_sim = WavefunctionSimulator()

def imprimir_wavefunction(wf, descripcion=""):
    """Imprime la función de onda de forma legible"""
    print(f"\n{descripcion}")
    print("=" * 60)
    amplitudes = wf.amplitudes
    for i, amp in enumerate(amplitudes):
        if np.abs(amp) > 1e-10:  # Solo mostrar amplitudes significativas
            print(f"|{i}>: {amp:.6f}")
    print("=" * 60)

def extraer_matriz(gate_func, gate_name):
    """Extrae la matriz de una puerta cuántica"""
    print(f"\n{'#' * 60}")
    print(f"MATRIZ DE LA PUERTA {gate_name}")
    print('#' * 60)

    prog = Program()
    prog += gate_func

    try:
        matriz = program_unitary(prog, n_qubits=1)
        print(f"\nMatriz de {gate_name}:")
        print(matriz)
        return matriz
    except Exception as e:
        print(f"Error al extraer matriz: {e}")
        return None

print("=" * 70)
print("PRÁCTICA: PUERTAS CUÁNTICAS DE UN QÚBIT")
print("=" * 70)

# =============================================================================
# PARTE 1: PUERTAS DE FASE (PHASE, S, T)
# =============================================================================

print("\n" + "=" * 70)
print("PARTE 1: PUERTAS DE FASE")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1.1 PUERTA PHASE con ángulo π/2
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("1.1 PUERTA PHASE(π/2)")
print("*" * 70)

angle_phase = np.pi / 2

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_phase_0 = Program()
prog_phase_0 += I(0)  # Identidad para mantener |0>

wf_inicial_0 = wf_sim.wavefunction(prog_phase_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de PHASE (estado |0>)")

# Aplicar PHASE
prog_phase_0.inst(PHASE(angle_phase, 0))
wf_final_0 = wf_sim.wavefunction(prog_phase_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de PHASE (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_phase_1 = Program()
prog_phase_1 += X(0)  # Aplicar X para obtener |1>

wf_inicial_1 = wf_sim.wavefunction(prog_phase_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de PHASE (estado |1>)")

# Aplicar PHASE
prog_phase_1.inst(PHASE(angle_phase, 0))
wf_final_1 = wf_sim.wavefunction(prog_phase_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de PHASE (estado |1>)")

# Extraer matriz de PHASE
extraer_matriz(PHASE(angle_phase, 0), "PHASE(π/2)")

# -----------------------------------------------------------------------------
# 1.2 PUERTA S
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("1.2 PUERTA S")
print("*" * 70)

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_s_0 = Program()
prog_s_0 += I(0)

wf_inicial_0 = wf_sim.wavefunction(prog_s_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de S (estado |0>)")

prog_s_0.inst(S(0))
wf_final_0 = wf_sim.wavefunction(prog_s_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de S (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_s_1 = Program()
prog_s_1 += X(0)

wf_inicial_1 = wf_sim.wavefunction(prog_s_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de S (estado |1>)")

prog_s_1.inst(S(0))
wf_final_1 = wf_sim.wavefunction(prog_s_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de S (estado |1>)")

# Extraer matriz de S
extraer_matriz(S(0), "S")

# -----------------------------------------------------------------------------
# 1.3 PUERTA T
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("1.3 PUERTA T")
print("*" * 70)

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_t_0 = Program()
prog_t_0 += I(0)

wf_inicial_0 = wf_sim.wavefunction(prog_t_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de T (estado |0>)")

prog_t_0.inst(T(0))
wf_final_0 = wf_sim.wavefunction(prog_t_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de T (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_t_1 = Program()
prog_t_1 += X(0)

wf_inicial_1 = wf_sim.wavefunction(prog_t_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de T (estado |1>)")

prog_t_1.inst(T(0))
wf_final_1 = wf_sim.wavefunction(prog_t_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de T (estado |1>)")

# Extraer matriz de T
extraer_matriz(T(0), "T")

# -----------------------------------------------------------------------------
# Análisis de relaciones entre puertas
# -----------------------------------------------------------------------------
print("\n\n" + "=" * 70)
print("ANÁLISIS: RELACIONES ENTRE PUERTAS DE FASE")
print("=" * 70)

print("\nRELACIONES OBSERVADAS:")
print("-" * 70)
print("• Puerta S = PHASE(π/2)")
print("• Puerta T = PHASE(π/4)")
print("• Puerta Z (Pauli Z) = PHASE(π) = S²")
print("\nMatrices teóricas:")
print("\nPHASE(θ) = [[1, 0], [0, e^(iθ)]]")
print("S = [[1, 0], [0, i]]")
print("T = [[1, 0], [0, e^(iπ/4)]]")
print("Z = [[1, 0], [0, -1]]")

# =============================================================================
# PARTE 2: PUERTAS DE ROTACIÓN (RX, RY, RZ)
# =============================================================================

print("\n\n" + "=" * 70)
print("PARTE 2: PUERTAS DE ROTACIÓN")
print("=" * 70)

angle_rot = np.pi / 4  # Ángulo de rotación para las pruebas

# -----------------------------------------------------------------------------
# 2.1 PUERTA RX (Rotación en eje X)
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("2.1 PUERTA RX(π/4)")
print("*" * 70)

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_rx_0 = Program()
prog_rx_0 += I(0)

wf_inicial_0 = wf_sim.wavefunction(prog_rx_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de RX (estado |0>)")

prog_rx_0.inst(RX(angle_rot, 0))
wf_final_0 = wf_sim.wavefunction(prog_rx_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de RX (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_rx_1 = Program()
prog_rx_1 += X(0)

wf_inicial_1 = wf_sim.wavefunction(prog_rx_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de RX (estado |1>)")

prog_rx_1.inst(RX(angle_rot, 0))
wf_final_1 = wf_sim.wavefunction(prog_rx_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de RX (estado |1>)")

# Extraer matriz de RX
extraer_matriz(RX(angle_rot, 0), "RX(π/4)")

# -----------------------------------------------------------------------------
# 2.2 PUERTA RY (Rotación en eje Y)
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("2.2 PUERTA RY(π/4)")
print("*" * 70)

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_ry_0 = Program()
prog_ry_0 += I(0)

wf_inicial_0 = wf_sim.wavefunction(prog_ry_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de RY (estado |0>)")

prog_ry_0.inst(RY(angle_rot, 0))
wf_final_0 = wf_sim.wavefunction(prog_ry_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de RY (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_ry_1 = Program()
prog_ry_1 += X(0)

wf_inicial_1 = wf_sim.wavefunction(prog_ry_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de RY (estado |1>)")

prog_ry_1.inst(RY(angle_rot, 0))
wf_final_1 = wf_sim.wavefunction(prog_ry_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de RY (estado |1>)")

# Extraer matriz de RY
extraer_matriz(RY(angle_rot, 0), "RY(π/4)")

# -----------------------------------------------------------------------------
# 2.3 PUERTA RZ (Rotación en eje Z)
# -----------------------------------------------------------------------------
print("\n\n" + "*" * 70)
print("2.3 PUERTA RZ(π/4)")
print("*" * 70)

# Estado inicial |0>
print("\n--- Estado inicial |0> ---")
prog_rz_0 = Program()
prog_rz_0 += I(0)

wf_inicial_0 = wf_sim.wavefunction(prog_rz_0)
imprimir_wavefunction(wf_inicial_0, "Función de onda ANTES de RZ (estado |0>)")

prog_rz_0.inst(RZ(angle_rot, 0))
wf_final_0 = wf_sim.wavefunction(prog_rz_0)
imprimir_wavefunction(wf_final_0, "Función de onda DESPUÉS de RZ (estado |0>)")

# Estado inicial |1>
print("\n--- Estado inicial |1> ---")
prog_rz_1 = Program()
prog_rz_1 += X(0)

wf_inicial_1 = wf_sim.wavefunction(prog_rz_1)
imprimir_wavefunction(wf_inicial_1, "Función de onda ANTES de RZ (estado |1>)")

prog_rz_1.inst(RZ(angle_rot, 0))
wf_final_1 = wf_sim.wavefunction(prog_rz_1)
imprimir_wavefunction(wf_final_1, "Función de onda DESPUÉS de RZ (estado |1>)")

# Extraer matriz de RZ
extraer_matriz(RZ(angle_rot, 0), "RZ(π/4)")

# -----------------------------------------------------------------------------
# Resumen de matrices de rotación
# -----------------------------------------------------------------------------
print("\n\n" + "=" * 70)
print("RESUMEN: MATRICES DE ROTACIÓN")
print("=" * 70)

print("\nFórmulas teóricas de las puertas de rotación:")
print("-" * 70)
print("\nRX(θ) = [[cos(θ/2), -i·sin(θ/2)],")
print("         [-i·sin(θ/2), cos(θ/2)]]")
print("\nRY(θ) = [[cos(θ/2), -sin(θ/2)],")
print("         [sin(θ/2), cos(θ/2)]]")
print("\nRZ(θ) = [[e^(-iθ/2), 0],")
print("         [0, e^(iθ/2)]]")

print("\n" + "=" * 70)
print("FIN DE LA PRÁCTICA")
print("=" * 70)
