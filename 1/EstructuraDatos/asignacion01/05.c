
#include <stdio.h>

#include <stdio.h>

int main() {
    int i, j, k, l, size;
    printf("Ingrese el tamaño del rombo: ");
    scanf("%d", &size);
    if (size >= 2 && size <= 10) {
            for (i = 1; i <= size; i++) {
        for (j = 1; j <= size - i; j++) {
            printf(" ");
        }
        for (k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    for (i = size - 1; i >= 1; i--) {
        for (l = 1; l <= size - i; l++) {
            printf(" ");
        }
        for (k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    } else {
        printf("No es un alto de la flecha válido");
    }
    printf("\n");
    return 0;
}
