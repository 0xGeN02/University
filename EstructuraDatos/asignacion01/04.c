#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    printf("Ingrese un numero entero impar >= a 3:\n");
    scanf("%d", &n);
    if (n >= 3 && n % 2 == 1) {
        for (i = 1; i <= (n + 1) / 2; i++) {
            for (j = 1; j <= i; j++) {
                printf("* ");
            }
            printf("\n");
        }
        for (i = (n - 1) / 2; i >= 1; i--) {
            for (j = 1; j <= i; j++) {
                printf("* ");
            }
            printf("\n");
        }
    } else {
        printf("Ingresa los datos en el rango [3, n) y recuerda que n pertenece a 2x+1 \n");
    }
    return 0;
}