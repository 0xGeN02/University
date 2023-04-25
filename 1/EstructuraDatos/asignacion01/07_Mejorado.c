#include <stdio.h>
#include <stdlib.h>

float suma_array(float arr[], int n) {
    if (n == 0) {
        return 0;
    }
    return arr[n - 1] + suma_array(arr, n - 1);
}

int main() {
    int n, i;
    float arr[100];
    printf("Ingrese el tamaño del arreglo (máximo 100): ");
    if (scanf("%d", &n) != 1 || n < 1 || n > 100) {
        printf("Entrada inválida.\n");
        exit(1);
    }
    printf("Ingrese los elementos del arreglo: \n");
    for (i = 0; i < n; i++) {
        if (scanf("%f", &arr[i]) != 1) {
            printf("Entrada inválida.\n");
            exit(1);
        }
    }
    printf("La suma de los elementos del arreglo es %.2f\n", suma_array(arr, n));
    return 0;
}
/*
Define una función recursiva llamada suma_array, que toma como argumentos un arreglo arr de números reales y un número entero n que representa el tamaño del arreglo.

En la función suma_array, si n es igual a 0, regresa 0.

En caso contrario, regresa el último elemento del arreglo (arr[n - 1]) más la llamada recursiva a la función suma_array con n-1.

En la función main, se pide al usuario que ingrese el tamaño del arreglo y sus elementos.

Se llama a la función suma_array para obtener la suma de los elementos del arreglo.

Finalmente, se imprime el resultado de la suma.
*/