#include <stdio.h>
#include <stdlib.h>

int main(){
    int height;
    printf("Ingrese la altura entre el 2 y el 10:\n");
    scanf("%d", &height);
    if(height <= 10 && height >= 2){
        const char* bricks = "**********";
        const char* space = "          ";
        for(int i=1; i<height+1; ++i)
        {
            printf("%*.*s      %.*s\n", height,i,bricks, i,space);
        }
    }
    else{
        printf("Vuelve a ingresar los datos en el rango [2,10]\n");
    }        
    return 0;
}
