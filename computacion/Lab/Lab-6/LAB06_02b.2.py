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
# Métodos Getters
    def Get_Asignatura(self):
        return (self.Asignatura)
    def Get_Nombre(self):
        return (self.Nombre)      

# PROBAR GETTERS DE LA CLASE ESTUDIANTE
E=Estudiante(12)    # 12 Actividades de evaluación 
E.Set_Asignatura(input("Nombre de la asignatura : "))
E.Set_Nombre(input("Nombre del estudiante   : "))
a=E.Get_Asignatura()
n=E.Get_Nombre()
print("Atributo \"Asignatura\" : \tValor : ",a)
print("Atributo  \"Nombre\"     : \tValor : ",n)