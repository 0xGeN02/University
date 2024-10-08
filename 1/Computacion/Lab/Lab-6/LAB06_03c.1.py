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
    def Set_AE(self,C):  # Ponderación
        self.AE=C
    def Set_Pondera(self,P):  # Ponderación
        self.Pondera=P
    def Set_Notas(self,CAL):  # Guardar notas
        self.Nota=CAL
# PROBAR CLASE ESTUDIANTE
Num_AE=12
E=Estudiante(Num_AE)
Cate=["Par 1","Par 2","Par 3","Test ","Tarea","Labor","Proye","Expos","Foros","Calid","Tutor","Práct"]
Pond=[10,20,10,10,10,10,15,5,5,2,2,1]
Notas=[7,9,7,6,6,4,8,8,1,1,1,0]
E.Set_AE(Cate)
E.Set_Pondera(Pond)
E.Set_Notas(Notas)
print("Actividad :",E.AE[2],"\t Nota : ",E.Nota[2],"\t Ponderación : ",E.Pondera[2])