#include <stdio.h>
#include <stdlib.h>
main(){
    int i, j, k;
    printf("Ingrese la altura entre el 2 y el 10:\n");
    scanf("%d", &k);
    if(k <= 10 && k >= 2){    
        for (i = 0; i < k; i++){
            for (j =  0; j <= i; j++){
                printf("* ");
            }
        printf("\n");
        }
    }
    else{
        printf("Vuelve a ingresar los datos en el rango [2,10]\n");
    }    
    return 0;
}