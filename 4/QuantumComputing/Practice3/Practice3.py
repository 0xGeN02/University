#!/usr/bin/env python3
"""
Práctica Simplificada - Siguiendo exactamente el flujo especificado
Computación Cuántica - Sesión 04
"""

import numpy as np
from pyquil import Program, get_qc
from pyquil.gates import *
import math

def main():
    # Configurar QVM
    qc = get_qc('1q-qvm')
    
    print("=" * 50)
    print("PRIMERA PARTE: PUERTAS DE FASE")
    print("=" * 50)
    
    # ===== PUERTA PHASE =====
    print("\n1. PUERTA PHASE con ángulo π/3")
    angle = math.pi / 3
    
    # Estado inicial |0⟩
    print("\n--- Estado inicial |0⟩ ---")
    prog_0 = Program()
    print("a. Programa definido con estado |0⟩")
    
    wf_0_initial = qc.wavefunction(prog_0)
    print("b. Función de onda inicial:", wf_0_initial.amplitudes)
    
    prog_0.inst(PHASE(angle, 0))
    print("c. Puerta PHASE añadida")
    
    wf_0_final = qc.wavefunction(prog_0)
    print("d. Función de onda final:", wf_0_final.amplitudes)
    
    # Estado inicial |1⟩
    print("\n--- Estado inicial |1⟩ ---")
    prog_1 = Program()
    prog_1.inst(X(0))  # Preparar estado |1⟩
    print("a. Programa definido con estado |1⟩")
    
    wf_1_initial = qc.wavefunction(prog_1)
    print("b. Función de onda inicial:", wf_1_initial.amplitudes)
    
    prog_1.inst(PHASE(angle, 0))
    print("c. Puerta PHASE añadida")
    
    wf_1_final = qc.wavefunction(prog_1)
    print("d. Función de onda final:", wf_1_final.amplitudes)
    
    # Calcular matriz
    print("\nMatriz de PHASE(π/3):")
    matrix_phase = np.column_stack([wf_0_final.amplitudes, wf_1_final.amplitudes])
    print(matrix_phase)
    
    # ===== PUERTA S =====
    print("\n2. PUERTA S")
    
    # Estado inicial |0⟩
    print("\n--- Estado inicial |0⟩ ---")
    prog_0_s = Program()
    wf_0_s_initial = qc.wavefunction(prog_0_s)
    print("Función de onda inicial:", wf_0_s_initial.amplitudes)
    
    prog_0_s.inst(S(0))
    wf_0_s_final = qc.wavefunction(prog_0_s)
    print("Función de onda final:", wf_0_s_final.amplitudes)
    
    # Estado inicial |1⟩
    print("\n--- Estado inicial |1⟩ ---")
    prog_1_s = Program()
    prog_1_s.inst(X(0))
    wf_1_s_initial = qc.wavefunction(prog_1_s)
    print("Función de onda inicial:", wf_1_s_initial.amplitudes)
    
    prog_1_s.inst(S(0))
    wf_1_s_final = qc.wavefunction(prog_1_s)
    print("Función de onda final:", wf_1_s_final.amplitudes)
    
    # Calcular matriz
    print("\nMatriz de S:")
    matrix_s = np.column_stack([wf_0_s_final.amplitudes, wf_1_s_final.amplitudes])
    print(matrix_s)
    
    # ===== PUERTA T =====
    print("\n3. PUERTA T")
    
    # Estado inicial |0⟩
    print("\n--- Estado inicial |0⟩ ---")
    prog_0_t = Program()
    wf_0_t_initial = qc.wavefunction(prog_0_t)
    print("Función de onda inicial:", wf_0_t_initial.amplitudes)
    
    prog_0_t.inst(T(0))
    wf_0_t_final = qc.wavefunction(prog_0_t)
    print("Función de onda final:", wf_0_t_final.amplitudes)
    
    # Estado inicial |1⟩
    print("\n--- Estado inicial |1⟩ ---")
    prog_1_t = Program()
    prog_1_t.inst(X(0))
    wf_1_t_initial = qc.wavefunction(prog_1_t)
    print("Función de onda inicial:", wf_1_t_initial.amplitudes)
    
    prog_1_t.inst(T(0))
    wf_1_t_final = qc.wavefunction(prog_1_t)
    print("Función de onda final:", wf_1_t_final.amplitudes)
    
    # Calcular matriz
    print("\nMatriz de T:")
    matrix_t = np.column_stack([wf_0_t_final.amplitudes, wf_1_t_final.amplitudes])
    print(matrix_t)
    
    print("\n" + "=" * 50)
    print("SEGUNDA PARTE: PUERTAS DE ROTACIÓN")
    print("=" * 50)
    
    rotation_angle = math.pi / 4
    
    # ===== PUERTA RX =====
    print(f"\n1. PUERTA RX con ángulo π/4")
    
    # Estado inicial |0⟩
    print("\n--- Estado inicial |0⟩ ---")
    prog_0_rx = Program()
    wf_0_rx_initial = qc.wavefunction(prog_0_rx)
    print("Función de onda inicial:", wf_0_rx_initial.amplitudes)
    
    prog_0_rx.inst(RX(rotation_angle, 0))
    wf_0_rx_final = qc.wavefunction(prog_0_rx)
    print("Función de onda final:", wf_0_rx_final.amplitudes)
    
    # Estado inicial |1⟩
    print("\n--- Estado inicial |1⟩ ---")
    prog_1_rx = Program()
    prog_1_rx.inst(X(0))
    wf_1_rx_initial = qc.wavefunction(prog_1_rx)
    print("Función de onda inicial:", wf_1_rx_initial.amplitudes)
    
    prog_1_rx.inst(RX(rotation_angle, 0))
    wf_1_rx_final = qc.wavefunction(prog_1_rx)
    print("Función de onda final:", wf_1_rx_final.amplitudes)
    
    print("\nMatriz de RX(π/4):")
    matrix_rx = np.column_stack([wf_0_rx_final.amplitudes, wf_1_rx_final.amplitudes])
    print(matrix_rx)
    
    # ===== PUERTA RY =====
    print(f"\n2. PUERTA RY con ángulo π/4")
    
    # Estado inicial |0⟩
    prog_0_ry = Program()
    wf_0_ry_initial = qc.wavefunction(prog_0_ry)
    print("Función de onda inicial:", wf_0_ry_initial.amplitudes)
    
    prog_0_ry.inst(RY(rotation_angle, 0))
    wf_0_ry_final = qc.wavefunction(prog_0_ry)
    print("Función de onda final:", wf_0_ry_final.amplitudes)
    
    # Estado inicial |1⟩
    prog_1_ry = Program()
    prog_1_ry.inst(X(0))
    wf_1_ry_initial = qc.wavefunction(prog_1_ry)
    print("Función de onda inicial:", wf_1_ry_initial.amplitudes)
    
    prog_1_ry.inst(RY(rotation_angle, 0))
    wf_1_ry_final = qc.wavefunction(prog_1_ry)
    print("Función de onda final:", wf_1_ry_final.amplitudes)
    
    print("\nMatriz de RY(π/4):")
    matrix_ry = np.column_stack([wf_0_ry_final.amplitudes, wf_1_ry_final.amplitudes])
    print(matrix_ry)
    
    # ===== PUERTA RZ =====
    print(f"\n3. PUERTA RZ con ángulo π/4")
    
    # Estado inicial |0⟩
    prog_0_rz = Program()
    wf_0_rz_initial = qc.wavefunction(prog_0_rz)
    print("Función de onda inicial:", wf_0_rz_initial.amplitudes)
    
    prog_0_rz.inst(RZ(rotation_angle, 0))
    wf_0_rz_final = qc.wavefunction(prog_0_rz)
    print("Función de onda final:", wf_0_rz_final.amplitudes)
    
    # Estado inicial |1⟩
    prog_1_rz = Program()
    prog_1_rz.inst(X(0))
    wf_1_rz_initial = qc.wavefunction(prog_1_rz)
    print("Función de onda inicial:", wf_1_rz_initial.amplitudes)
    
    prog_1_rz.inst(RZ(rotation_angle, 0))
    wf_1_rz_final = qc.wavefunction(prog_1_rz)
    print("Función de onda final:", wf_1_rz_final.amplitudes)
    
    print("\nMatriz de RZ(π/4):")
    matrix_rz = np.column_stack([wf_0_rz_final.amplitudes, wf_1_rz_final.amplitudes])
    print(matrix_rz)
    
    print("\n" + "=" * 50)
    print("ANÁLISIS DE RELACIONES")
    print("=" * 50)
    print("S = PHASE(π/2)")
    print("T = PHASE(π/4)")  
    print("Z = PHASE(π)")
    print("Las puertas S y T son casos especiales de PHASE")

if __name__ == "__main__":
    main()
