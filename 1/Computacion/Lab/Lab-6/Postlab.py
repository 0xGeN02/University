# Post-Laboratorio 06
# Asignación 10
# Realizado por Equipo (5)
#Mateo Delgado, Mónica de Paula, Hugo Cabero, Miguel Abelairas, Mario Baños


import CLASE_ESTUDIANTE as CE
# Programa para un estudiante con 3 asignaturas

# Asignatura 1
Num_AE=12
E=CE.Estudiante(Num_AE)
E.Set_Asignatura("Programación")
E.Set_Nombre("Bernardo Quindimil Micó")
DATA=CE.mat.Entrada_CSV("DATA01.csv",str)
E.Set_AE(CE.mat.Columa_Vector_M(DATA,0))
E.Set_Pondera(CE.mat.Columa_Vector_M(DATA,1))
E.Set_Notas(CE.mat.Columa_Vector_M(DATA,2))
print("Estudiante : ",E.Get_Nombre())
print("Asignatura : ",E.Get_Asignatura())
print("Actividades de Evaluación y Calificaciones")
E.Muestra_Notas()
print("Calificación Final : {:2.2f}".format(E.Nota_Final()))

# Asignatura 2
E=CE.Estudiante(Num_AE)
E.Set_Asignatura("Estructuras Empresariales")
E.Set_Nombre("Bernardo Quindimil Micó")
DATA1=CE.mat.Entrada_CSV("DATA02.csv",str)
E.Set_AE(CE.mat.Columa_Vector_M(DATA1,0))
E.Set_Pondera(CE.mat.Columa_Vector_M(DATA1,1))
E.Set_Notas(CE.mat.Columa_Vector_M(DATA1,2))
print("Estudiante : ",E.Get_Nombre())
print("Asignatura : ",E.Get_Asignatura())
print("Actividades de Evaluación y Calificaciones")
E.Muestra_Notas()
print("Calificación Final : {:2.2f}".format(E.Nota_Final()))

# Asignatura 3
E=CE.Estudiante(Num_AE)
E.Set_Asignatura("Matemáticas")
E.Set_Nombre("Mateo Delgado")
DATA2=CE.mat.Entrada_CSV("DATA03.csv",str)
E.Set_AE(CE.mat.Columa_Vector_M(DATA2,0))
E.Set_Pondera(CE.mat.Columa_Vector_M(DATA2,1))
E.Set_Notas(CE.mat.Columa_Vector_M(DATA2,2))
print("Estudiante : ",E.Get_Nombre())
print("Asignatura : ",E.Get_Asignatura())
print("Actividades de Evaluación y Calificaciones")
E.Muestra_Notas()
print("Calificación Final : {:2.2f}".format(E.Nota_Final()))