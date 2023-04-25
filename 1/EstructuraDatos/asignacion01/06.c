//Calculamos la función combinatoria simple

#include <stdio.h>

//Calculo Factorial
long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

//Calculo Combinatoria
long long combinatoria(int n, int x) {
    return factorial(n) / (factorial(x) * factorial(n - x));
}

//Regresar valores
int main() {
    int n, x;
    printf("Ingrese el número n: ");
    scanf("%d", &n);
    printf("Ingrese el número x: ");
    scanf("%d", &x);
    if( n >= x){
        printf("El valor de la combinatoria sin repetición C(%d,%d) es %lld\n", n, x, combinatoria(n, x));
    }
    else{
        printf("El valor x no puede ser superior al valor n");
    }
    return 0;
}