#include <stdio.h>

int main(void)    // Función principal
{
// Declaración de variables 
    double  pi=3.14159; 
    int    b=255; 
    printf ("El valor de pi usando\t e\t en el formato %e\n", pi); 
    printf ("El valor de pi usando\t f\t en el formato \n", pi); 
    printf ("El valor de pi usando\t g\t en el formato %g\n", pi); 
    printf ("El valor de pi usando\t f4.1\t en el formato %3.1f\n", pi); 
    printf ("El valor de pi usando\t f1.5\t en el formato %1.5f\n", pi); 
    printf ("El valor de b usando\t d\t en el formato %d\n", b);
    printf ("El valor de b usando\t o\t en el formato %o\n", b); 
    printf ("El valor de b usando\t x\t en el formato %x\n", b);  
return 0;   
}
