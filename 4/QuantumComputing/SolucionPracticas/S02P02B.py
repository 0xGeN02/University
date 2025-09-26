from pyquil import get_qc, Program
from pyquil.gates import H

prog = Program(H(0),H(1),H(2),H(3)).wrap_in_numshots_loop(50)
ro = prog.declare('ro','BIT',4)

print(prog)

prog.measure_all()

qvm = get_qc('9q-square-qvm')
result = qvm.run(qvm.compile(prog), 0).get_register_map().get("ro")

cara = 0
cruz = 0
for res in result:
 print(res)

 if res[0] == 0:
  cara += 1
 else:
  cruz += 1

 if res[1] == 0:
  cara += 1
 else:
  cruz += 1

 if res[2] == 0:
  cara += 1
 else:
  cruz += 1

 if res[3] == 0:
  cara += 1
 else:
  cruz += 1

print(cara)
print(cruz)
if cara > cruz:
 print("gana A")
elif cara == cruz:
 print("empate")
else:
 print("gana B")
