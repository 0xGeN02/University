#include <stdio.h>

//Funcion Fibo
int fibonacci(int n) {
    if (n < 0) {
        printf("Entrada inválida. Debe ser un número positivo.\n");
    return -1;
    } 
    else if (n == 0 || n == 1) {
        return n;
    } 
    else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int n, resultado;
    printf("Ingrese un número para calcular su n-ésimo número en la sucesión de Fibonacci: ");
    scanf("%d", &n);
    resultado = fibonacci(n);
    if (resultado != -1) {
        printf("El %d-ésimo número en la sucesión de Fibonacci es %d\n", n, resultado);
    }
    return 0;
}

/*
El código realiza una función recursiva que calcula el valor de la sucesión de Fibonacci para un número dado. La función tiene una validación de entrada, lo que significa que verifica que el número ingresado sea válido antes de proceder con el cálculo.

La función Fibonacci se basa en la definición matemática de la sucesión, en la que F(0) = F(1) = 1 y F(n) = F(n-1) + F(n-2). La función recursiva hace llamadas a sí misma con n-1 y n-2 hasta que n sea igual a 0 o 1, momento en el cual se regresa 1.

En el main, se pide al usuario que ingrese un número y se llama a la función de Fibonacci para obtener su valor en la sucesión. Finalmente, se imprime el resultado.
*/