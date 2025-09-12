"""
    1st State of Bell (|Φ⁺⟩)

    In this state, both qubits are entangled and have the same value.
    The state can be represented as:
    |Φ⁺⟩ = (|00⟩ + |11⟩) / √2
"""
from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 2),
    H(0), # H -> superposition |0> -> (|0> + |1>)/sqrt(2)
    CNOT(0, 1), # CNOT -> entanglement
    MEASURE(0, ("ro", 0)), # Measure qubit 0 and store result in classical bit 0
    MEASURE(1, ("ro", 1)) # Measure qubit 1 and store result in classical bit 1
).wrap_in_numshots_loop(100) # Run the program 100 times to get statistics

qvm = get_qc("9q-square-qvm") # Use a 9-qubit square QVM
result = qvm.run(qvm.compile(prog)).get_register_map().get("ro")
for r in result:
    print(r)
