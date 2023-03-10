#include <stdlib.h>
#include <stdio.h>
//1) Cuadrado

char cuadrado(){
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

//2)Triangulo Rectangulo Izquierdo

char TrianguloIz(){
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

//3)Triangulo Rectangulo Derecho

char TrianguloDer(){
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

//4)Flecha

char flecha() {
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
        printf("Ingresa los datos en el rango [3,infinito) y recuerda que n pertenece a 2x+1 \n");
    }
    return 0;
}

//5)Rombo

char Rombo(){
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
//6)Factorial

int Factorial(){
        int i, j, k, size;
    printf("Ingrese el tamaño del rombo: ");
    scanf("%d", &size);
    if(size>=2 && size<=10){
        for (i = 1; i <= size; i++) {
            for (j = i; j < size; j++) {
                printf(" ");
            }
            for (k = 1; k < (i * 2); k++) {
                printf("*");
            }
            printf("\n");
        }
        for (i = size - 1; i >= 1; i--) {
            for (j = size; j > i; j--) {
                printf(" ");
            }
            for (k = 1; k < (i * 2); k++) {
                printf("*");
            }
            printf("\n");
        }
    }
    else{
        printf("No es un alto del rombo válido");
    }
    return 0;
}
//7)Arrays unidimensionales

//Calculo Factorial
long long print_factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * Factorial(n - 1);
}

//Calculo Combinatoria
long long combinatoria(int n, int x) {
    return Factorial(n) / (Factorial(x) * Factorial(n - x));
}

//Regresar valores
long long Array() {
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

//7.b)Array con filtrado de datos

float suma_array(float arr[], int n) {
    if (n == 0) {
        return 0;
    }
    return arr[n - 1] + suma_array(arr, n - 1);
}

long long ArrayFiltros() {
    int n, i;
    float arr[100];
    printf("Ingrese el tamaño del arreglo (máximo 100): ");
    if (scanf("%d", &n) != 1 || n < 1 || n > 100) {
        printf("Entrada inválida.\n");
        exit(1);
    }
    printf("Ingrese los elementos del arreglo: \n");
    for (i = 0; i < n; i++) {
        if (scanf("%f", &arr[i]) != 1) {
            printf("Entrada inválida.\n");
            exit(1);
        }
    }
    printf("La suma de los elementos del arreglo es %.2f\n", suma_array(arr, n));
    return 0;
}
/*
Define una función recursiva llamada suma_array, que toma como argumentos un arreglo arr de números reales y un número entero n que representa el tamaño del arreglo.

En la función suma_array, si n es igual a 0, regresa 0.

En caso contrario, regresa el último elemento del arreglo (arr[n - 1]) más la llamada recursiva a la función suma_array con n-1.

En la función main, se pide al usuario que ingrese el tamaño del arreglo y sus elementos.

Se llama a la función suma_array para obtener la suma de los elementos del arreglo.

Finalmente, se imprime el resultado de la suma.
*/

//8)Fibonacci

#include <stdio.h>

//Funcion Fibo
int fibonacci(int n) {
    if (n < 0) {
        printf("Entrada inválida. Debe ser un número positivo.\n");
    return -1;
    } 
    else if (n == 0 || n == 1) {
        return n;
    } 
    else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int fibonacci() {
    int n, resultado;
    printf("Ingrese un número para calcular su n-ésimo número en la sucesión de Fibonacci: ");
    scanf("%d", &n);
    resultado = fibonacci(n);
    if (resultado != -1) {
        printf("El %d-ésimo número en la sucesión de Fibonacci es %d\n", n, resultado);
    }
    return 0;
}

/*
El código realiza una función recursiva que calcula el valor de la sucesión de Fibonacci para un número dado. La función tiene una validación de entrada, lo que significa que verifica que el número ingresado sea válido antes de proceder con el cálculo.

La función Fibonacci se basa en la definición matemática de la sucesión, en la que F(0) = F(1) = 1 y F(n) = F(n-1) + F(n-2). La función recursiva hace llamadas a sí misma con n-1 y n-2 hasta que n sea igual a 0 o 1, momento en el cual se regresa 1.

En el main, se pide al usuario que ingrese un número y se llama a la función de Fibonacci para obtener su valor en la sucesión. Finalmente, se imprime el resultado.
*/

//RETO_1 Triangulo Pascal

long factorial(int);

int Pascal(){
        int i, n, c;

        printf("Ingresa el número de filas que desea ver en el triángulo pascal: \n");
        scanf("%d",&n);

        for (i = 0; i < n; i++)
        {
            for (c = 0; c <= (n - i - 2); c++){
                printf(" ");
            }

            for (c = 0 ; c <= i; c++){
                printf("%ld ", factorial(i)/(factorial(c)*factorial(i-c)));
            }

            printf("\n");
        }

        return 0;
    }

    long factorial(int n){
        int c;
        long result = 1;

        for (c = 1; c <= n; c++){
            result = result*c;
        }
        return result;
}

//RETO_2 Hanoi

void Hanoi(int discos, char origen, char destino, char auxiliar) {
    if (discos == 1) {
        printf("Mover disco 1 desde %c hasta %c\n", origen, destino);
        return;
    }
    Hanoi(discos - 1, origen, auxiliar, destino);
    printf("Mover disco %d desde %c hasta %c\n", discos, origen, destino);
    Hanoi(discos - 1, auxiliar, destino, origen);
}

int Print_Hanoi() {
    int discos;
    printf("Ingrese el número de discos (3-8): ");
    scanf("%d", &discos);
    if (discos<3 || discos>8){
        printf("Indique una cantidad comprendida en (3,8)");
    }
    else{
        Hanoi(discos, 'A', 'C', 'B');
    }
    return 0;
}