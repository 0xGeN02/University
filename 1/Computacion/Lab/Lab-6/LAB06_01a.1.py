import sys
import Modulo_Matrices as mat
# CLASE ESTUDIANTE
class Estudiante:
    # Constructor de la clase
    def __init__(self) -> None:
        self.Asignatura =''
        self.Nombre     =''
        self.AE         =[]
        self.Nota       =[]
        self.Pondera    =[]
    
# PROBAR CLASE ESTUDIANTE
E=Estudiante()
print("E es tipo : ",type(E),"  Ubicado en : ",id(E))
print("Tipo de Atributo    \"Asignatura\"  : ",type(E.Nombre),"\tValor : ",E.Nombre)
print("Tipo de Atributo    \"Nombre\"      : ",type(E.Nombre),"\tValor : ",E.Nombre)
print("Tipo de Atributo    \"AE\"          : ",type(E.AE),"\tValor : ",E.AE)
print("Tipo de Atributo    \"Nota\"        : ",type(E.Nota),"\tValor : ",E.Nota)
print("Tipo de Atributo    \"Pondera\"     : ",type(E.Pondera),"\tValor : ",E.Pondera)