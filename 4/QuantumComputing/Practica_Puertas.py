"""
Práctica S07 - Computación Cuántica
Puertas Multiqúbit: SWAP, Controladas, CSWAP y Toffoli
Implementación con PyQuil
Profesor: Yago González Rozas
"""

from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Measurement
import numpy as np

print("="*80)
print("PRÁCTICA S07 - PUERTAS MULTIQÚBIT (PyQuil)")
print("="*80)

# Crear simulador cuántico
qc = get_qc('9q-square-qvm')

# ============================================================================
# PARTE 1: PUERTA SWAP
# ============================================================================

print("\n" + "="*80)
print("PARTE 1: PUERTA SWAP")
print("="*80)

# Estados iniciales posibles para 2 qubits
estados_2q = ['00', '01', '10', '11']

print("\n--- Tarea 1.1: Mediciones antes y después de SWAP ---")

for estado in estados_2q:
    print(f"\n>>> Estado inicial: |{estado}>")
    
    # Crear programa ANTES de SWAP
    p_antes = Program()
    
    # Preparar estado inicial
    if estado[0] == '1':
        p_antes += X(0)
    if estado[1] == '1':
        p_antes += X(1)
    
    # Medición
    ro_antes = p_antes.declare('ro', 'BIT', 2)
    p_antes += MEASURE(0, ro_antes[0])
    p_antes += MEASURE(1, ro_antes[1])
    p_antes.wrap_in_numshots_loop(1000)
    
    # Ejecutar
    resultado_antes = qc.run(p_antes)
    mediciones_antes = resultado_antes.readout_data.get('ro')
    estado_antes = f"{int(mediciones_antes[0][0])}{int(mediciones_antes[0][1])}"
    print(f"   Antes de SWAP: |{estado_antes}>")
    
    # Crear programa DESPUÉS de SWAP
    p_despues = Program()
    
    # Preparar estado inicial
    if estado[0] == '1':
        p_despues += X(0)
    if estado[1] == '1':
        p_despues += X(1)
    
    # Aplicar SWAP
    p_despues += SWAP(0, 1)
    
    # Medición
    ro_despues = p_despues.declare('ro', 'BIT', 2)
    p_despues += MEASURE(0, ro_despues[0])
    p_despues += MEASURE(1, ro_despues[1])
    p_despues.wrap_in_numshots_loop(1000)
    
    # Ejecutar
    resultado_despues = qc.run(p_despues)
    mediciones_despues = resultado_despues.readout_data.get('ro')
    estado_despues = f"{int(mediciones_despues[0][0])}{int(mediciones_despues[0][1])}"
    print(f"   Después de SWAP: |{estado_despues}>")
    print(f"   Interpretación: Los qubits intercambian sus estados")

print("\n--- Tarea 1.2: Reversibilidad de SWAP ---")
print("\nDemostración matemática de que SWAP es reversible:")
print("Una puerta es reversible si U × U† = I (identidad)")

# Matriz SWAP
swap_matrix = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])

print("\nMatriz SWAP:")
print(swap_matrix)

# SWAP × SWAP
swap_squared = np.matmul(swap_matrix, swap_matrix)
print("\nSWAP × SWAP:")
print(swap_squared)

# Verificar si es identidad
is_identity = np.allclose(swap_squared, np.eye(4))
print(f"\n¿SWAP × SWAP = Identidad? {is_identity}")
print("Por tanto, SWAP es su propia inversa (autoinversa) y es reversible.")

# Verificación práctica
print("\nVerificación práctica: SWAP aplicado dos veces:")
p_doble_swap = Program()
p_doble_swap += X(0)  # Estado inicial |10>
print(f"Estado inicial: |10>")
p_doble_swap += SWAP(0, 1)
p_doble_swap += SWAP(0, 1)  # Aplicar SWAP dos veces
ro = p_doble_swap.declare('ro', 'BIT', 2)
p_doble_swap += MEASURE(0, ro[0])
p_doble_swap += MEASURE(1, ro[1])
p_doble_swap.wrap_in_numshots_loop(100)
resultado = qc.run(p_doble_swap)
mediciones = resultado.readout_data.get('ro')
estado_final = f"{int(mediciones[0][0])}{int(mediciones[0][1])}"
print(f"Después de 2 SWAPs: |{estado_final}> (vuelve al estado original)")

# ============================================================================
# PARTE 2: PUERTAS CONTROLADAS
# ============================================================================

print("\n" + "="*80)
print("PARTE 2: PUERTAS CONTROLADAS")
print("="*80)

print("\n--- Tarea 2.1: Puertas CU con diferentes estados iniciales ---")

# Lista de puertas controladas
puertas_info = [
    ('CNOT (CX)', CNOT),
    ('CY', lambda c, t: Program(RY(np.pi/2, t), CNOT(c, t), RY(-np.pi/2, t))),
    ('CZ', CZ)
]

for nombre_puerta, puerta_func in puertas_info:
    print(f"\n>>> Puerta {nombre_puerta}")
    
    for estado in estados_2q:
        print(f"\n   Estado inicial: |{estado}> (q0=control, q1=objetivo)")
        
        # ANTES de aplicar puerta
        p_antes = Program()
        if estado[0] == '1':
            p_antes += X(0)
        if estado[1] == '1':
            p_antes += X(1)
        
        ro_antes = p_antes.declare('ro', 'BIT', 2)
        p_antes += MEASURE(0, ro_antes[0])
        p_antes += MEASURE(1, ro_antes[1])
        p_antes.wrap_in_numshots_loop(100)
        
        resultado = qc.run(p_antes)
        mediciones = resultado.readout_data.get('ro')
        antes = f"{int(mediciones[0][0])}{int(mediciones[0][1])}"
        print(f"      Antes: |{antes}>")
        
        # DESPUÉS de aplicar puerta
        p_despues = Program()
        if estado[0] == '1':
            p_despues += X(0)
        if estado[1] == '1':
            p_despues += X(1)
        
        # Aplicar puerta controlada
        if callable(puerta_func):
            if nombre_puerta == 'CY':
                p_despues += puerta_func(0, 1)
            else:
                p_despues += puerta_func(0, 1)
        
        ro_despues = p_despues.declare('ro', 'BIT', 2)
        p_despues += MEASURE(0, ro_despues[0])
        p_despues += MEASURE(1, ro_despues[1])
        p_despues.wrap_in_numshots_loop(100)
        
        resultado = qc.run(p_despues)
        mediciones = resultado.readout_data.get('ro')
        despues = f"{int(mediciones[0][0])}{int(mediciones[0][1])}"
        print(f"      Después: |{despues}>")

print("\n--- Tarea 2.2: Estados de Bell ---")
print("\nCreando los 4 estados de Bell y realizando 10 mediciones:")

estados_bell = [
    ("Φ+", lambda: Program(H(0), CNOT(0, 1))),
    ("Φ-", lambda: Program(X(1), H(0), CNOT(0, 1))),
    ("Ψ+", lambda: Program(X(0), H(0), CNOT(0, 1))),
    ("Ψ-", lambda: Program(X(0), X(1), H(0), CNOT(0, 1)))
]

for nombre, crear_bell in estados_bell:
    print(f"\n>>> Estado de Bell |{nombre}>")
    
    resultados_mediciones = []
    for i in range(10):
        p = crear_bell()
        ro = p.declare('ro', 'BIT', 2)
        p += MEASURE(0, ro[0])
        p += MEASURE(1, ro[1])
        p.wrap_in_numshots_loop(1)
        
        resultado = qc.run(p)
        mediciones = resultado.readout_data.get('ro')
        medicion = f"{int(mediciones[0][0])}{int(mediciones[0][1])}"
        resultados_mediciones.append(medicion)
        print(f"   Medición {i+1}: |{medicion}>")
    
    print(f"   Relación: Los qubits están ENTRELAZADOS")
    print(f"   Observación: Miden siempre correlacionados (00/11 o 01/10)")

print("\n--- Tarea 2.3: SWAP con CNOTs ---")
print("\nCircuito SWAP usando solo puertas CNOT:")

p_swap_cnot = Program()
# Estado inicial de ejemplo |10>
p_swap_cnot += X(0)
print("Estado inicial: |10>")

# SWAP = CNOT(0,1) + CNOT(1,0) + CNOT(0,1)
p_swap_cnot += CNOT(0, 1)
p_swap_cnot += CNOT(1, 0)
p_swap_cnot += CNOT(0, 1)

ro = p_swap_cnot.declare('ro', 'BIT', 2)
p_swap_cnot += MEASURE(0, ro[0])
p_swap_cnot += MEASURE(1, ro[1])
p_swap_cnot.wrap_in_numshots_loop(100)

print("\nCircuito:")
print(p_swap_cnot)

resultado = qc.run(p_swap_cnot)
mediciones = resultado.readout_data.get('ro')
estado_final = f"{int(mediciones[0][0])}{int(mediciones[0][1])}"
print(f"\nResultado: |{estado_final}>")
print("Se obtiene |01>, confirmando que SWAP = 3 CNOTs")

# ============================================================================
# PARTE 3: PUERTAS MULTICONTROLADAS
# ============================================================================

print("\n" + "="*80)
print("PARTE 3: PUERTAS MULTICONTROLADAS (CSWAP y TOFFOLI)")
print("="*80)

# Estados iniciales para 3 qubits
estados_3q = ['000', '001', '010', '011', '100', '101', '110', '111']

print("\n--- Tarea 3.1: CSWAP y Toffoli con diferentes estados ---")

print("\n>>> Puerta CSWAP (q0=control, q1 y q2 se intercambian)")
for estado in estados_3q:
    p = Program()
    
    # Preparar estado
    for i, bit in enumerate(estado):
        if bit == '1':
            p += X(i)
    
    # Aplicar CSWAP
    p += CSWAP(0, 1, 2)
    
    # Medición
    ro = p.declare('ro', 'BIT', 3)
    p += MEASURE(0, ro[0])
    p += MEASURE(1, ro[1])
    p += MEASURE(2, ro[2])
    p.wrap_in_numshots_loop(100)
    
    resultado = qc.run(p)
    mediciones = resultado.readout_data.get('ro')
    estado_final = f"{int(mediciones[0][0])}{int(mediciones[0][1])}{int(mediciones[0][2])}"
    print(f"   |{estado}> -> |{estado_final}>")

print("\n>>> Puerta TOFFOLI/CCNOT (q0,q1=controles, q2=objetivo)")
for estado in estados_3q:
    p = Program()
    
    # Preparar estado
    for i, bit in enumerate(estado):
        if bit == '1':
            p += X(i)
    
    # Aplicar Toffoli (CCNOT)
    p += CCNOT(0, 1, 2)
    
    # Medición
    ro = p.declare('ro', 'BIT', 3)
    p += MEASURE(0, ro[0])
    p += MEASURE(1, ro[1])
    p += MEASURE(2, ro[2])
    p.wrap_in_numshots_loop(100)
    
    resultado = qc.run(p)
    mediciones = resultado.readout_data.get('ro')
    estado_final = f"{int(mediciones[0][0])}{int(mediciones[0][1])}{int(mediciones[0][2])}"
    nota = " (NOT aplicado)" if estado[:2] == '11' else ""
    print(f"   |{estado}> -> |{estado_final}>{nota}")

print("\n--- Tarea 3.2: Construcción de puertas clásicas con Toffoli ---")

print("\n>>> Puerta NAND con Toffoli:")
print("NAND(a,b) = Toffoli con q2 inicializado en |1>")
print("Tabla de verdad:")
for a in [0, 1]:
    for b in [0, 1]:
        p = Program()
        if a == 1:
            p += X(0)
        if b == 1:
            p += X(1)
        p += X(2)  # Inicializar q2 en |1>
        p += CCNOT(0, 1, 2)
        
        ro = p.declare('ro', 'BIT', 1)
        p += MEASURE(2, ro[0])
        p.wrap_in_numshots_loop(1)
        
        resultado = qc.run(p)
        mediciones = resultado.readout_data.get('ro')
        salida = int(mediciones[0][0])
        print(f"   NAND({a},{b}) = {salida}")

print("\n>>> Puerta NOT con Toffoli:")
print("NOT(a) = Toffoli con q0,q1 en |1> y entrada en q2")
for a in [0, 1]:
    p = Program()
    p += X(0)
    p += X(1)
    if a == 1:
        p += X(2)
    p += CCNOT(0, 1, 2)
    
    ro = p.declare('ro', 'BIT', 1)
    p += MEASURE(2, ro[0])
    p.wrap_in_numshots_loop(1)
    
    resultado = qc.run(p)
    mediciones = resultado.readout_data.get('ro')
    salida = int(mediciones[0][0])
    print(f"   NOT({a}) = {salida}")

print("\n>>> Puerta AND con Toffoli:")
print("AND(a,b) = Toffoli con q2 inicializado en |0>")
for a in [0, 1]:
    for b in [0, 1]:
        p = Program()
        if a == 1:
            p += X(0)
        if b == 1:
            p += X(1)
        # q2 en |0> por defecto
        p += CCNOT(0, 1, 2)
        
        ro = p.declare('ro', 'BIT', 1)
        p += MEASURE(2, ro[0])
        p.wrap_in_numshots_loop(1)
        
        resultado = qc.run(p)
        mediciones = resultado.readout_data.get('ro')
        salida = int(mediciones[0][0])
        print(f"   AND({a},{b}) = {salida}")

print("\n>>> Puerta XOR con Toffoli:")
print("XOR requiere composición de múltiples Toffolis")
print("XOR(a,b) = (a OR b) AND NAND(a,b)")
print("Implementación más simple: usar CNOT directamente")

print("\n>>> Implicaciones:")
print("Que Toffoli pueda representar cualquier puerta clásica significa que:")
print("- La computación cuántica es AL MENOS tan potente como la clásica")
print("- Podemos usar computadoras cuánticas para hacer computación clásica reversible")
print("- Toffoli es UNIVERSALMENTE COMPLETA para computación clásica")
print("- Cualquier algoritmo clásico puede ejecutarse en una computadora cuántica")

print("\n--- Tarea 3.3: Toffoli con CNOTs y puertas básicas ---")
print("\nCircuito Toffoli descompuesto en puertas CNOT, H, T:")

p_toffoli = Program()
# Estado inicial |110> para probar
p_toffoli += X(0)
p_toffoli += X(1)
print("Estado inicial: |110>")

# Descomposición estándar de Toffoli
p_toffoli += H(2)
p_toffoli += CNOT(1, 2)
p_toffoli += RZ(-np.pi/4, 2)  # T-dagger
p_toffoli += CNOT(0, 2)
p_toffoli += RZ(np.pi/4, 2)   # T
p_toffoli += CNOT(1, 2)
p_toffoli += RZ(-np.pi/4, 2)  # T-dagger
p_toffoli += CNOT(0, 2)
p_toffoli += RZ(np.pi/4, 1)   # T en q1
p_toffoli += RZ(np.pi/4, 2)   # T en q2
p_toffoli += H(2)
p_toffoli += CNOT(0, 1)
p_toffoli += RZ(np.pi/4, 0)   # T en q0
p_toffoli += RZ(-np.pi/4, 1)  # T-dagger en q1
p_toffoli += CNOT(0, 1)

ro = p_toffoli.declare('ro', 'BIT', 3)
p_toffoli += MEASURE(0, ro[0])
p_toffoli += MEASURE(1, ro[1])
p_toffoli += MEASURE(2, ro[2])
p_toffoli.wrap_in_numshots_loop(100)

print("\nCircuito (descomposición completa):")
print("H(2) - CNOT(1,2) - Tdg(2) - CNOT(0,2) - T(2) - ...")
print("(6 CNOTs + puertas H, T)")

resultado = qc.run(p_toffoli)
mediciones = resultado.readout_data.get('ro')
estado_final = f"{int(mediciones[0][0])}{int(mediciones[0][1])}{int(mediciones[0][2])}"
print(f"\nResultado: |{estado_final}>")
print("Se obtiene |111>, confirmando que funciona como Toffoli")

print("\n" + "="*80)
print("FIN DE LA PRÁCTICA")
print("="*80)
print("\nNota: Para ejecutar este código necesitas:")
print("  pip install pyquil")
print("  Tener ejecutando el QVM de Rigetti: quilc -S y qvm -S")