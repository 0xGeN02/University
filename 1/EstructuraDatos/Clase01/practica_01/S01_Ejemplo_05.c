#include <stdio.h>      // Biblioteca estándar de entrada salida
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
int main(void){          // Función principal
    // Declaración de variables 
    int HE,ME,SE,HS,MS,SS;     //Declaracion de variables y constantes locales
    printf("Indique Hora     en Rango [0 - 23] : ");
    scanf("%d",&HE);
    printf("Indique Minutos  en Rango [0 - 59] : ");
    scanf("%d",&ME);
    printf("Indique Segundos en Rango [0 - 59] : ");
    scanf("%d",&SE);
    if ( SE!=59 ){
        HS=HE; MS=ME; SS=SE+1;
    }
    else{
        SS=0;
        if ( ME!=59 ){
            HS=HE; MS=ME+1;
        }
    else{
        MS=0;
        if (HE!=23)
            HS=HE+1;
        else
            HS=0;
        }
    }
    printf("\n");
    printf("*********   Salida    *********\n");
    printf("\tHora de Entrada\tH:M:S [%d:%d:%d]\n ",HE,ME,SE);
    printf("\tHora +1 Segundo\tH:M:S [%d:%d:%d]\n ",HS,MS,SS);
    return 0;
}