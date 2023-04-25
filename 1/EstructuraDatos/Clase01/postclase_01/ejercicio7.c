/*
#include <stdio.h>
#include <stdio.h>

#define SUCURSALES 4
#define PRODUCTOS 6

float ventas[SUCURSALES][PRODUCTOS];
float ingresos_sucursal[SUCURSALES];
float ingresos_empresa;

int sucursal_mayor_ingreso;
float mayor_ingreso_sucursal;
int producto_mayor_ingreso;
float mayor_ingreso_producto;
int producto_menor_ingreso;
float menor_ingreso_producto;

void ingresos() {
    int i, j;
    for (i = 0; i < SUCURSALES; i++) {
        for (j = 0; j < PRODUCTOS; j++) {
            ingresos_sucursal[i] += ventas[i][j];
            ingresos_empresa += ventas[i][j];
        }
    }

    sucursal_mayor_ingreso = 0;
    mayor_ingreso_sucursal = ingresos_sucursal[0];
    for (i = 1; i < SUCURSALES; i++) {
        if (ingresos_sucursal[i] > mayor_ingreso_sucursal) {
            sucursal_mayor_ingreso = i;
            mayor_ingreso_sucursal = ingresos_sucursal[i];
        }
    }

    producto_mayor_ingreso = 0;
    mayor_ingreso_producto = 0;
    producto_menor_ingreso = 0;
    menor_ingreso_producto = ingresos_sucursal[0];
    for (i = 0; i < SUCURSALES; i++) {
        for (j = 0; j < PRODUCTOS; j++) {
            if (ventas[i][j] > mayor_ingreso_producto) {
                producto_mayor_ingreso = j;
                mayor_ingreso_producto = ventas[i][j];
            }
            if (ventas[i][j] < menor_ingreso_producto) {
                producto_menor_ingreso = j;
                menor_ingreso_producto = ventas[i][j];
            }
        }
    }
}

void reporte() {
    printf("Ingresos de la empresa: %.2f euros\n", ingresos_empresa);

    int i;
    for (i = 0; i < SUCURSALES; i++) {
        printf("Ingresos de la sucursal %d: %.2f euros\n", i+1, ingresos_sucursal[i]);
    }

    printf("Sucursal con mayores ingresos: %d con %.2f euros\n", sucursal_mayor_ingreso+1, mayor_ingreso_sucursal);
    printf("Producto que genero mayores ingresos: %d con %.2f euros\n", producto_mayor_ingreso+1, mayor_ingreso_producto);
    printf("Producto que genero menores ingresos: %d con %.2f euros\n", producto_menor_ingreso+1, menor_ingreso_producto);
*/
#include <stdio.h>

struct empresa{
    int sucursal[4];
    int producto[6];
    float ventas[4][6];
};

int main()
{
    struct empresa comidaRapida;
    int i, j;
    float empresaTotal = 0.0, sucursalTotal = 0.0;
    int sucursalMayorIngreso = 0;
    int productoMayorIngreso = 0;
    int productoMenorIngreso = 0;
    float mayorIngreso = 0.0;
    float menorIngreso = 0.0;

    // Se ingresan los datos de las ventas de cada producto por sucursal
    for(i = 0; i < 4; i++){
        sucursalTotal = 0.0;
        printf("Ingrese los datos para la sucursal %d\n", i);
        for(j = 0; j < 6; j++){
            printf("Ventas del producto %d: ", j);
            scanf("%f", &comidaRapida.ventas[i][j]);
            sucursalTotal += comidaRapida.ventas[i][j];
            if(comidaRapida.ventas[i][j] > mayorIngreso){
                mayorIngreso = comidaRapida.ventas[i][j];
                productoMayorIngreso = j;
                sucursalMayorIngreso = i;
            }
            if(comidaRapida.ventas[i][j] < menorIngreso){
                menorIngreso = comidaRapida.ventas[i][j];
                productoMenorIngreso = j;
            }
        }
        printf("Total de ingresos de la sucursal %d: %f\n", i, sucursalTotal);
        empresaTotal += sucursalTotal;
    }

    printf("Total de ingresos de la empresa: %f\n", empresaTotal);
    printf("La sucursal con mayores ingresos es la %d\n", sucursalMayorIngreso);
    printf("El producto que generó mayores ingresos es el %d\n", productoMayorIngreso);
    printf("El producto que generó menores ingresos es el %d\n", productoMenorIngreso);

    return 0;
}