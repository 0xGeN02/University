import sys
import Modulo_Matrices as mat
# CLASE ESTUDIANTE
class Estudiante:
    # Constructor de la clase
        def __init__(self,nAE) -> None:
            self.NumAE      =nAE
            self.Asignatura =''
            self.Nombre     =''
            self.AE         =mat.vec.Crea_Vector_Valor(self.NumAE,' ')
            self.Nota       =mat.vec.Crea_Vector_Valor(self.NumAE,0.0)
            self.Pondera    =mat.vec.Crea_Vector_Valor(self.NumAE,0.0)

    
# PROBAR CLASE ESTUDIANTE
E=Estudiante(12)
print("E es tipo : ",type(E),"  Ubicado en : ",id(E))
print("Tipo de Atributo    \"Asignatura\"  : ",type(E.Nombre),"\tValor : ",E.Nombre)
print("Tipo de Atributo    \"Nombre\"      : ",type(E.Nombre),"\tValor : ",E.Nombre)
print("Tipo de Atributo    \"AE\"          : ",type(E.AE),"\tValor : ",E.AE)
print("Tipo de Atributo    \"Nota\"        : ",type(E.Nota),"\tValor : ",E.Nota)
print("Tipo de Atributo    \"Pondera\"     : ",type(E.Pondera),"\tValor : ",E.Pondera)
print("Tamaño del Atributo \"Asignatura\"  : ",len(E.Nombre))
print("Tamaño del Atributo \"Nombre\"      : ",len(E.Nombre))
print("Tamaño del Atributo \"AE\"          : ",len(E.AE))
print("Tamaño del Atributo \"Nota\"        : ",len(E.Nota))
print("Tamaño del Atributo \"Pondera\"     : ",len(E.Pondera))