#2.8
#Algoritmo Suma_Segundo
#Incrementar en un segundo una hora
#Definiciones y Declaraciones

#inicio

HF = int(input("Indique Horas "))
MF = int(input("Indique Minutos "))
SF = int(input("Indique Segundos "))

while(SF>59 or MF>59):

    if(SF <= 59):
        SF = SF

        if (MF <= 59):
            MF = MF
            HF = HF
        else:
            HF = HF+1
            MF = MF-60
    else:
        SF = SF-60
        MF = MF+1

        if (MF <= 59):
            MF = MF
            HF = HF
        else:
            HF = HF+1
            MF = MF-60

print("Hora final,", HF, MF, SF)
