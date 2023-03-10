#include <stdio.h>

int main() {
    int dia, mes, ano;
    int diasMes[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    printf("Ingrese una fecha en formato dd/mm/yyyy: ");
    scanf("%d/%d/%d", &dia, &mes, &ano);

    // Validación de datos de entrada
    if (dia < 1 || dia > 31 || mes < 1 || mes > 12 || ano < 1960 || ano > 2021) {
        printf("La fecha ingresada es inválida.\n");
        return 1;
    }

    // Ajuste de días del mes para anos bisiestos
    if (ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0)) {
        diasMes[1] = 29;
    }

    if (dia > diasMes[mes - 1]) {
        printf("La fecha ingresada es inválida.\n");
        return 1;
    }
    
    printf("La fecha ingresada es válida.\n");

    return 0;
}