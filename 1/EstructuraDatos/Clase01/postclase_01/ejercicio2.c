#include <stdio.h>

int main() {
    int horas1, minutos1, segundos1, horas2, minutos2, segundos2;
    int horasT, minutosT, segundosT;

    printf("Ingrese el tiempo T1 en formato hh:mm:ss: ");
    scanf("%d:%d:%d", &horas1, &minutos1, &segundos1);

    printf("Ingrese el tiempo T2 en formato hh:mm:ss: ");
    scanf("%d:%d:%d", &horas2, &minutos2, &segundos2);

    // Validación de datos de entrada
    if (horas1 < 0 || horas2 < 0 || minutos1 < 0 || minutos1 > 59 || minutos2 < 0 || minutos2 > 59 || segundos1 < 0 || segundos1 > 59 || segundos2 < 0 || segundos2 > 59) {
        printf("Los datos ingresados son inválidos.\n");
        return 1;
    }

    segundosT = segundos1 + segundos2;
    minutosT = minutos1 + minutos2;
    horasT = horas1 + horas2;

    // Ajuste de tiempo en caso de sobrepasar 59 segundos o 59 minutos
    minutosT += segundosT / 60;
    segundosT = segundosT % 60;

    horasT += minutosT / 60;
    minutosT = minutosT % 60;

    printf("Tiempo total: %d:%d:%d\n", horasT, minutosT, segundosT);
    return 0;
}