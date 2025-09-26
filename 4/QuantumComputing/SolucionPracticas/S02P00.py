from pyquil import get_qc, Program
from pyquil.gates import H

prog = Program(H(0))
ro = prog.declare('ro')

print(prog)

prog.measure(0,ro[0])

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog), 0).get_register_map().get("ro")

print(result[0])
if result[0] == 0:
 print("cara")
else:
 print("cruz")
