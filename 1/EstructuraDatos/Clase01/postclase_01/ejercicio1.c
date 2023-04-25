#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char** args){
    float a, b, c, disc, x1, x2, xi, xr;
    printf("\n\t\tSolucion de una ecuacion de segundo grado");
    printf("\n\t\t_________________________________________\n\n\n");
    printf("\t\t\tEscribe el valor de a --> ");
    scanf("%f", &a);
    printf("\t\t\tEscribe el valor de b --> ");
    scanf("%f", &b);
    printf("\t\t\tEscribe el valor de c --> ");
    scanf("%f", &c);
    disc=pow(b, 2.0)-4*a*c;
    if(a != 0 ){
        if(disc>0.0){
        printf("\t\t\tLas dos raices son reales");
        x1=((-b+sqrt(disc))/(2.0*a));
        x2=((-b-sqrt(disc))/(2.0*a));
        printf("\n\t\t\tx1=%.2f   x2=%.2f", x1, x2);
        }
        else if(disc=0.0){
            x1 =  -b/(2.0*a);
            printf("Solo existe 1 radicando o se puede considerar que x1=x2= \n", x1);
        }
        else{
            xr=(-b/(2.0*a));
            xi=(sqrt(-disc)/(2.0*a));
            printf("\n\t\tLa raiz real es %.2f y la imaginaria es %.2f", xr, xi);
        }
    }
    else if (a == 0.0 && b != 0.0){
        x1 = c/b; 
        printf("solo existe 1 radicando: \n", x1); 
    }
    else if(a == 0.0 && b == 0.0){
        printf("No exsiste raiz ya que no existen monomios");
        }
    printf("\n\n\t\t\t");
}
