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
    def Muestra_Notas(self):
        print("Estudiante : ",self.Nombre)
        for i in range(len(self.Nota)):
            print("Categoría: {0}\tCalificación: {1:2.2f} \tPonderación: {2}"
            .format(self.AE[i],float(self.Nota[i]),self.Pondera[i])) 
        print() 
# PROBAR CLASE ESTUDIANTE
Num_AE=12
E=Estudiante(Num_AE)
DATA=mat.Entrada_CSV("DATA01.csv",str)
E.Set_AE(mat.Columa_Vector_M(DATA,0))
E.Set_Pondera(mat.Columa_Vector_M(DATA,1))
E.Set_Notas(mat.Columa_Vector_M(DATA,2))
E.Muestra_Notas()