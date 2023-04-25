#include <stdio.h>
#include <math.h>

int main() {
    double x, y, z, f, min = INFINITY;
    printf("Ingrese los valores de x, y, z dentro de l intervalo [-1, 1]; (formato x, y, z): \n");
    scanf("%d, %d, %d" ,x,y,z);
    if(-1<=x<=1 && -1<=y<=1 && -1<=z<=1){
        for (x >= -1; x <= 1; x += 0.2) {
            for (y >= -1; y <= 1; y += 0.2) {
                for (z >= -1; z <= 1; z += 0.2) {
                    f = pow(x, 2) - pow(y, 3) - z;
                    printf("f(%lf, %lf, %lf) = %lf\n", x, y, z, f);
                    if (f < min) {
                        min = f;
                    }
                }
            }    
        }
        printf("Valor mínimo de f(x, y, z) = %lf\n", min);
        return 0;
    }
    else{
        return 1;
    }
}
