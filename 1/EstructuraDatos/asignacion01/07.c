#include <stdio.h>
//Suma Array
float suma_array(float arr[], int n) {
    if (n == 0) {
        return 0;
    }
    return arr[n - 1] + suma_array(arr, n - 1);
}

//Procesamiento de data
int main() {
    int n, i;
    float arr[100];
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);
    printf("Ingrese los elementos del arreglo: \n");
    for (i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
    }
    printf("La suma de los elementos del arreglo es %.2f\n", suma_array(arr, n));
    return 0;
}
/*
La función suma_array se encarga de sumar los elementos de un arreglo de números reales.
El argumento arr es el arreglo de números reales y el argumento n es el tamaño del arreglo.
La función recursiva hace una llamada a sí misma con n-1 hasta que n sea igual a 0, momento en el cual se regresa 0.
En el main, se pide al usuario que ingrese el tamaño del arreglo y sus elementos.
Se llama a la función suma_array para obtener la suma de los elementos del arreglo.
Se imprime el resultado final de la suma de los elementos del arreglo.
*/