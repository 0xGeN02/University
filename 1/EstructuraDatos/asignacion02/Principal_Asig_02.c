
//Grupo 5: Hugo Iglesias; Manuel Menendez; Laura Vazquez; Manuel Mateo Delgado; Juan Ramon Pazo
//Programa hecho por: Manuel Mateo Delgado
//Asignacion 2 Estructura de Datos
//Universidad Intercontinental de la Empresa

//Include
#include "Biblio_Asig_02.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Muestra menu de opciones 
void Mostrar_Opciones(){
    printf("\033[2J"); // Limpia terminal codigos de escape (ANSI X3.64) 
    printf("\033[36m***************  GESTION DE UNA LISTA   ******************\n");
    printf("*                                                         *\n");
    printf("*      Agregar un Tren al Origen    ...........   1       *\n");
    printf("*      Agregar Tren en una Posicion ...........   2       *\n");
    printf("*      Buscar y Data del Tren       ...........   3       *\n");
    printf("*      Editar Datos del Tren        ...........   4       *\n");
    printf("*      Modiificar Estado del Tren   ...........   5       *\n");
    printf("*      Mostrar Ubicacion del Tren   ...........   6       *\n");
    printf("*      Lista Orden Ubicacion        ...........   7       *\n");
    printf("*      Mostrar Tren y Yuxtapuestos  ...........   8       *\n");
    printf("*      Retirar Nodo                 ...........   9       *\n");
    printf("*      Reingresar Nodo              ...........   10      *\n");
    printf("*      Eliminar Nodo                ...........   11      *\n");
    printf("*      Angulo Azimuth               ...........   12      *\n");
    printf("*      Distancia Nodo               ...........   13      *\n");
    printf("*      Invertir Lista               ...........   14      *\n");
    printf("*      Finalizar                    ...........   15      *\n");
    printf("*                                                         *\n");
    printf("\033[36m***********************************************************\n");

    
}

// Declare the Menu function
int Menu(int n1, int n2);

//Retornamos una opcion valida del Menu_Opciones()
int Menu(int n1, int n2){

	int opcion;
  	do{
	 	Mostrar_Opciones();
		printf(" \033[31mIndique su opcion : ");
		scanf("%d",&opcion);
	}
	while (opcion<n1 || opcion>n2);
    return opcion;
}


//Funcion Main

int main() {
    int opcion;
    
    char codigo_busqueda[9];
    char codigo1, codigo2;

    struct Data data;
    struct Nodo *nodo = NULL;
    struct Nodo *nodo_Asig = NULL;
    struct Nodo *nodo_retirado = NULL;
    struct Nodo *nodo1 = NULL, *nodo2 = NULL;

    do {
        Menu(1, 15);
        printf("\033[33mIngrese una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                // Crea un nuevo nodo al inicio
                Crear_Nodo(&nodo, data);
                printf("\033[32mTren agregado correctamente.\n");

                // Imprime datos para corroborar que esten correctos
                Imprimir_Nodo(nodo);
                break;

            case 2:
                // Crea un nuevo nodo en una posicion dada
                printf("\033[32mIngrese la posicion en la que desea agregar el tren: ");
                int posicion;
                scanf("%d", &posicion);

                // Crea un nuevo nodo con la informacion del tren
                printf("\033[32mIngrese el codigo del tren: ");
                scanf("%s", data.codigo);
                printf("\033[32mIngrese la ubicacion del tren (latitud, longitud): ");
                scanf("(%f, %f)", &data.latitud, &data.longitud);

                // Inserta el nuevo nodo en la posicion especificada
                Insertar_Nodo_Posicion(&nodo, data, posicion);

                printf("\033[32mTren agregado correctamente.\n");
                break;

            case 3:
                // Buscar nodo en la lista enlazada
                printf("\033[32mIngrese el codigo del tren que desea buscar: ");
                scanf("%s", data.codigo);

                struct Nodo *nodo_encontrado = Buscar_Nodo(data.codigo, nodo);
                if (nodo_encontrado != NULL) {
                    printf("\033[32mNodo encontrado:\n");
                    Imprimir_Nodo(nodo_encontrado);
                } else {
                    printf("\033[32mNo se encontro el nodo con el codigo especificado.\n");
                }
                break;

            case 4:
                // Editar datos de un nodo
                printf("\033[32mIngrese el codigo del tren que desea editar: ");
                scanf("%s", data.codigo);

                struct Nodo *nodo_a_editar = Buscar_Nodo(data.codigo, nodo);
                if (nodo_a_editar != NULL) {
                    Insertar_Data(&data);
                    if (strcmp(data.codigo, nodo_a_editar->Data.codigo) == 0) {
                        Editar_Data_Nodo(nodo_a_editar, data);
                        printf("\033[32mLa data del nodo ha sido actualizada correctamente.\n");
                    } else {
                        printf("\033[32mEl codigo ingresado no coincide con el codigo del nodo a editar.\n");
                    }
                } else {
                    printf("\033[32mNo se encontro el nodo con el codigo especificado.\n");
                }
            break;

            case 5: // Cambiar estado de un nodo
                printf("\033[32mIngrese el codigo del tren que desea cambiar de estado: ");
                scanf("%s", &codigo_busqueda[9]);
                nodo_Asig = Buscar_Nodo(codigo_busqueda, nodo);
                if (nodo_Asig != NULL) {
                    int nuevo_estado;
                    printf("\033[32mIngrese el nuevo estado del tren (0 = Detenido, 1 = En movimiento, 2 = En espera, 3 = En reparacion): ");
                    scanf("%d", &nuevo_estado);
                    if (nuevo_estado >= 0 && nuevo_estado <= 3) {
                        nodo_Asig->Data.estado = nuevo_estado;
                        printf("\033[32mEl estado del nodo ha sido actualizado correctamente.\n");
                    } else {
                        printf("\033[32mEl estado ingresado no es valido.\n");
                    }
                } else {
                    printf("\033[32mNo se encontro el nodo con el codigo especificado.\n");
                }
            break;

            case 6: // Mostrar nodo y ubicacion en formato grados, minutos, segundos
                printf("\033[32mIngrese el codigo del tren que desea mostrar: ");
                scanf("%s", &codigo_busqueda[9]);
                nodo_Asig = Buscar_Nodo(codigo_busqueda, nodo);
                if (nodo_Asig != NULL) {
                printf("\033[32mInformacion del nodo:\n");
                Print_Nodo_Ubicacion(nodo_Asig);
                } else {
                printf("\033[32mNo se encontro el nodo con el codigo especificado.\n");
                }
            break;


            case 7: // Lista Ordenada
                printf("\033[32mLista de codigos de trenes ordenados alfabeticamente:\n");
                Mostrar_Codigos_Ordenados(nodo);
            break;

            case 8: // Mostrar Nodos Yuxtapuestos
                if (nodo == NULL) {
                    printf("\033[32mLa lista esta vacia.\n");
                } else {
                    int i = 1;
                    while (nodo != NULL) {
                        printf("%d. Codigo: %s\n", i, nodo->Data.codigo);
                        nodo = nodo->siguiente;
                        i++;
                    }
                    printf("\033[32mIngrese el numero del nodo del que desea mostrar los nodos yuxtapuestos: ");
                    int opcion;
                    scanf("%d", &opcion);
                    if (opcion < 1 || opcion >= i) {
                        printf("\033[32mLa opcion ingresada no es valida.\n");
                    } else {
                        for (int j = 1; j < opcion; j++) {
                            nodo = nodo->siguiente;
                        }
                        printf("\033[32mInformacion del nodo seleccionado:\n");
                        Mostrar_Nodo_yuxtapuestos(nodo);
                    }
                }
            break;

        case 9: // Retirar nodo
            if (nodo == NULL) {
                printf("\033[32mLa lista esta vacia.\n");
            } else {
                char codigo[9];
                printf("\033[32mIngrese el codigo del nodo a retirar: ");
                scanf("%s", codigo);
                struct Nodo *nodo_a_retirar = Buscar_Nodo(codigo, nodo);
                if (nodo_a_retirar == NULL) {
                    printf("\033[32mEl nodo con codigo %s no se encuentra en la lista.\n", codigo);
                } else {
                    Retirar_Nodo(nodo_a_retirar);
                    printf("\033[32mEl nodo con codigo %s ha sido retirado de la lista.\n", codigo);
                    nodo_retirado = nodo_a_retirar;
                }
            }
        break;
        case 10: // Reingresar nodo
            if (nodo_retirado == NULL) {
                printf("\033[32mNo hay nodos retirados para reingresar.\n");
            } else {
                printf("\033[32mNodos retirados:\n");
                int i = 1;
                struct Nodo *nodo_actual = nodo_retirado;
                while (nodo_actual != NULL) {
                    printf("\033[32m%d. Codigo: %s\n", i, nodo_actual->Data.codigo);
                    nodo_actual = nodo_actual->siguiente;
                    i++;
                }
                printf("\033[32mSeleccione el numero del nodo que desea reingresar: ");
                int opcion;
                scanf("%d", &opcion);
                if (opcion < 1 || opcion >= i) {
                    printf("\033[32mLa opcion ingresada no es valida.\n");
                } else {
                    nodo_actual = nodo_retirado;
                    struct Nodo *nodo_anterior = NULL;
                    for (int j = 1; j < opcion; j++) {
                        nodo_anterior = nodo_actual;
                        nodo_actual = nodo_actual->siguiente;
                    }
                    if (nodo_anterior == NULL) {
                        nodo_retirado = nodo_actual->siguiente;
                    } else {
                        nodo_anterior->siguiente = nodo_actual->siguiente;
                    }
                    Reingresar_Nodo(nodo_retirado, nodo_anterior, nodo_actual);
                    printf("\033[32mEl nodo con codigo %s ha sido reingresado a la lista.\n", nodo_actual->Data.codigo);
                }
            }
        break;

        case 11: // Eliminar nodo retirado
            if (nodo_retirado == NULL) {
                printf("\033[32mNo hay nodos retirados para eliminar.\n");
            } else {
                printf("\033[32mNodos retirados:\n");
                int i = 1;
                struct Nodo *nodo_actual = nodo_retirado;
                while (nodo_actual != NULL) {
                    printf("\033[32m%d. Codigo: %s\n", i, nodo_actual->Data.codigo);
                    nodo_actual = nodo_actual->siguiente;
                    i++;
                }
                printf("\033[32mSeleccione el numero del nodo que desea eliminar: ");
                int opcion;
                scanf("%d", &opcion);
                if (opcion < 1 || opcion >= i) {
                    printf("\033[32mLa opcion ingresada no es valida.\n");
                } else {
                    nodo_actual = nodo_retirado;
                    struct Nodo *nodo_eliminar;
                    if (opcion == 1) {
                        nodo_eliminar = nodo_retirado;
                        nodo_retirado = nodo_retirado->siguiente;
                    } else {
                        for (int j = 1; j < opcion - 1; j++) {
                            nodo_actual = nodo_actual->siguiente;
                        }
                        nodo_eliminar = nodo_actual->siguiente;
                        nodo_actual->siguiente = nodo_actual->siguiente->siguiente;
                    }
                    printf("\033[32mEl nodo con codigo %s ha sido eliminado de la lista de nodos retirados.\n", nodo_eliminar->Data.codigo);
                    Eliminar_Nodo(nodo_eliminar);
                }
            }
        break;

            case 12://Azimuth
                if (nodo == NULL) {
                    printf("\033[32mLa lista esta vacia.\n");
                } else {
                    char codigo1[9], codigo2[9];
                    printf("\033[32mIngrese el codigo del primer nodo: ");
                    scanf("%s", codigo1);
                    printf("\033[32mIngrese el codigo del segundo nodo: ");
                    scanf("%s", codigo2);
                    struct Nodo *nodo1 = Buscar_Nodo(codigo1, nodo1);
                    struct Nodo *nodo2 = Buscar_Nodo(codigo2, nodo2);
                    if (nodo1 == NULL || nodo2 == NULL) {
                    printf("\033[32mUno o ambos nodos no se encuentran en la lista.\n");
                    } else {
                    Calcular_Angulo_Azimuth(nodo1, nodo2);
                    }
                }
                break;
                
            case 13: // Distancia Nodos

                printf("\033[32mIngrese el codigo del primer nodo: ");
                scanf("%s", &codigo1);

                nodo1 = Buscar_Nodo(&codigo1, nodo);

                if (nodo1 == NULL) {
                    printf("\033[32mEl nodo" "%d" "no existe en la lista.\n", codigo1);
                    break;
                }

                printf("\033[32mIngrese el codigo del segundo nodo: ");
                scanf("%s", &codigo2);

                nodo2 = Buscar_Nodo(&codigo2, nodo);

                if (nodo2 == NULL) {
                    printf("\033[32mEl nodo %d no existe en la lista.\n", codigo2);
                    break;
                }

                // Distancia Vectorial
                Distancia_Nodos(nodo1, nodo2);
                printf("\n");

                // Distancia Haversine
                Distancia_Haversine(nodo1, nodo2);
                printf("\n");
                
                //Eliminamos los punteros de memoria
                free(nodo1);
                free(nodo2);
            break;
            
            case 14://Invertir Lista
            
                printf("\033[32mCrear lista invertida\n");
                Crear_Lista_Invertida(&nodo);
                printf("\033[32mLista invertida creada exitosamente.\n");
            break;

            case 15://Finalizar
                printf("\033[32mPrograma finalizado.\n");
                VaciarLista(&nodo);
                break;
            default:
                printf("\033[31mOpcion invalida.\n");
                break;
        }
        printf("\033[35mPresione una tecla para continuar");
    } while (opcion != 15);

    return 0;
}