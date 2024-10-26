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
# Métodos Setters
    def Set_Asignatura(self,Asig):  # Guardar nombre
        self.Asignatura=Asig   
    def Set_Nombre(self,Nom):  # Guardar nombre
        self.Nombre=Nom    
 
# PROBAR SETTERS DE LA CLASE ESTUDIANTE
E=Estudiante(12)      # 12 Actividades de Evaluación
E.Set_Asignatura("Programación")
E.Set_Nombre("Eladio Dapena Gonzalez")
print("Atributo \"Asignatura\" : \tValor : ",E.Asignatura)
print("Atributo  \"Nombre\"     : \tValor : ",E.Nombre)
E.Set_Asignatura(input("Nombre de la asignatura : "))
E.Set_Nombre(input("Nombre del estudiante   : "))
print("Atributo \"Asignatura\" : \tValor : ",E.Asignatura)
print("Atributo  \"Nombre\"     : \tValor : ",E.Nombre)