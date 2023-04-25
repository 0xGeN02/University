#include <stdio.h>

int main() {
    int i;
    double temp, minTemp = 100, maxTemp = -100, totalTemp = 0, promedio;
    int minMuestra, maxMuestra;

    for (i = 1; i <= 24; i++) {
        printf("Ingrese la temperatura de la muestra %d: ", i);
        scanf("%lf", &temp);
        printf("Temperatura de la muestra %d: %.2lf\n", i, temp);
        if (temp < minTemp) {
            minTemp = temp;
            minMuestra = i;
        }
        if (temp > maxTemp) {
            maxTemp = temp;
            maxMuestra = i;
        }
        totalTemp += temp;
    }

    promedio = totalTemp / 24;

    printf("Menor temperatura: %.2lf (muestra %d)\n", minTemp, minMuestra);
    printf("Mayor temperatura: %.2lf (muestra %d)\n", maxTemp, maxMuestra);
    printf("Promedio de las temperaturas: %.2lf\n", promedio);
    return 0;
}