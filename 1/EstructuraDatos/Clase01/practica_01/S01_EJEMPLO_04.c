#include <stdio.h>

int main(void){
// Declaración de variables locales 
    float base,altura,area;        	// Variables locales    
    printf("Base = ");              		// Salida   
    scanf("%f",&base);            		 // Entrada teclado 
    printf("Altura = ");           		// Salida
    scanf("%f",altura);            	               // Entrada teclado 
    area = base*altura/2.0;         	// Operación aritmética y asignación
    printf("Area = %6.2f\n",area);  	// Salida   
    return 0;                          	// Retorno
}
