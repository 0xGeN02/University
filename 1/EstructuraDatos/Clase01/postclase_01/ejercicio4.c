#include <stdio.h>

int main() {
    int cantidad;
    double numero, suma = 0, sumaCuadrados = 0;

    printf("Ingrese la cantidad de números a procesar: ");
    scanf("%d", &cantidad);

    for (int i = 1; i <= cantidad; i++) {
        printf("Ingrese el número %d: ", i);
        scanf("%lf", &numero);

        // Validación de número no negativo
        if (numero < 0) {
            printf("Los números deben ser no negativos.\n");
            return 1;
        }

        suma += numero;
        sumaCuadrados += numero * numero;
    }

    printf("Sumatoria de cuadrados: %lf\n", sumaCuadrados);
    printf("Promedio de los números: %lf\n", suma / cantidad);
    printf("Promedio de los cuadrados: %lf\n", sumaCuadrados / cantidad);

    return 0;
}