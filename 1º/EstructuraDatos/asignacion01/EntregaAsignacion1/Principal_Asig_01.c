#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Biblio_Asig_01.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <function_name>\n", argv[0]);
        return 1;
    }

    // Get the function name from the command line arguments
    char *function_name = argv[1];

    // Use a switch statement to call the chosen function
    if (strcmp(function_name, "cuadrado") == 0) {
        cuadrado();
    }
    else if (strcmp(function_name, "TrianguloIz") == 0) {
        TrianguloIz();
    }
    
    else if (strcmp(function_name, "TrianguloDer") == 0) {
        TrianguloDer();
    }
    else if (strcmp(function_name, "flecha") == 0) {
        flecha();
    }
    else if (strcmp(function_name, "Rombo") == 0) {
        Rombo();
    }
    else if (strcmp(function_name, "Factorial") == 0) {
        if (argc < 3) {
            printf("Usage: %s Factorial <n>\n", argv[0]);
            return 1;
        }
        int n = atoi(argv[2]);
        printf("Factorial(%d) = %lld\n", n, print_factorial(n));
    }
    else if (strcmp(function_name, "combinatoria") == 0) {
        if (argc < 4) {
            printf("Usage: %s combinatoria <n> <x>\n", argv[0]);
            return 1;
        }
        int n = atoi(argv[2]);
        int x = atoi(argv[3]);
        printf("C(%d,%d) = %lld\n", n, x, combinatoria(n, x));
    }
    else if (strcmp(function_name, "Array") == 0) {
        Array();
    }
    else if (strcmp(function_name, "ArrayFiltros") == 0) {
        ArrayFiltros();
    }
    else if (strcmp(function_name, "Fibo") == 0) {
        if (argc < 3) {
            printf("Usage: %s Fibo <n>\n", argv[0]);
            return 1;
        }
        int n = atoi(argv[2]);
        for (int i = 0; i <= n; i++) {
            printf("%d ", Fibo(i));
        }
        printf("\n");
    }
    else if (strcmp(function_name, "Pascal") == 0) {
        Pascal();
    }
    else if (strcmp(function_name, "Hanoi") == 0) {
        if (argc < 3) {
            printf("Usage: %s Hanoi <discos>\n", argv[0]);
            return 1;
        }
        int discos = atoi(argv[2]);
        Hanoi(discos, 'A', 'C', 'B');
    }
    else {
        printf("Error: invalid function name\n");
        return 1;
    }

    return 0;
}