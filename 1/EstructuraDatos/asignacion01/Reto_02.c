#include <stdio.h>

void Hanoi(int discos, char origen, char destino, char auxiliar) {
    if (discos == 1) {
        printf("Mover disco 1 desde %c hasta %c\n", origen, destino);
        return;
    }
    Hanoi(discos - 1, origen, auxiliar, destino);
    printf("Mover disco %d desde %c hasta %c\n", discos, origen, destino);
    Hanoi(discos - 1, auxiliar, destino, origen);
}

int main() {
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