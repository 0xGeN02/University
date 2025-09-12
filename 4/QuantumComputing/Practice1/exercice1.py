from pyquil import Program
from pyquil.gates import I
from pyquil.api import WavefunctionSimulator

prog = Program(I(0))

qvm = WavefunctionSimulator()
result = qvm.wavefunction(prog)
print(result)
