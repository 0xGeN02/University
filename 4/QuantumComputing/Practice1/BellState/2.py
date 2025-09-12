"""
 2nd State of Bell (|Φ⁻⟩)

    In this state, both qubits are entangled and have the same value,
    but with a negative sign in the superposition.
    The state can be represented as:
    |Φ⁻⟩ = (|00⟩ - |11⟩) / √2
"""
from pyquil import Program, get_qc
from pyquil.gates import X, H, CNOT, MEASURE
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 2),
    X(0),        # Primero X para cambiar la fase
    H(0),        # Luego Hadamard para crear superposición
    CNOT(0, 1),  # CNOT para entrelazar
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1))
).wrap_in_numshots_loop(100)

qvm = get_qc("9q-square-qvm")
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")
for r in result:
    print(r)
