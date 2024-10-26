#include <stdlib.h>
#include <stdio.h>

main(){
    int i,j,k; 
    printf("Ingrese el tamano de filas entre el 2 y el 10:\n");
    scanf("%d", &k);

    if(k <= 10 && k >=2){
        for (j = 0; j < k; j++){
            for(i = 0; i < k; i++){
                printf("* ");
            }
            printf("\n");
        }
    }
    else{
        printf("El tamano de filas no puede ser menor o igual a 1 ni superior a 10");
    }
    return 0;
}

