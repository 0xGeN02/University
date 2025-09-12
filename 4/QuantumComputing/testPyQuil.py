from pyquil import get_qc, Program
from pyquil.gates import H, CNOT, MEASURE

# Creamos un programa cuántico
p = Program()
ro = p.declare('ro', 'BIT', 2)

# Hadamard en q0 y CNOT de q0 a q1
p += H(0)
p += CNOT(0, 1)

# Medimos ambos qubits
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])

# Conectamos con el simulador de 2 qubits
qc = get_qc("2q-qvm")

# Ejecutamos el programa varias veces
result = qc.run(p.wrap_in_numshots_loop(10))
print("Resultados:", result)
