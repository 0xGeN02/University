import CLASE_ESTUDIANTE as CE
# PROBAR CLASE ESTUDIANTE
Num_AE=12
E=CE.Estudiante(Num_AE)
E.Set_Asignatura("Programación")
E.Set_Nombre("ESCRIBE TU NOMBRE AQUI")
DATA=CE.mat.Entrada_CSV("DATA01.csv",str)
E.Set_AE(CE.mat.Columa_Vector_M(DATA,0))
E.Set_Pondera(CE.mat.Columa_Vector_M(DATA,1))
E.Set_Notas(CE.mat.Columa_Vector_M(DATA,2))
print("Estudiante : ",E.Get_Nombre())
print("Asignatura : ",E.Get_Asignatura())
print("Actividades de Evaluación y Calificaciones")
E.Muestra_Notas()
print("Calificación Final : {:2.2f}".format(E.Nota_Final()))