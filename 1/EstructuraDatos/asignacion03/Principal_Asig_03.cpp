#include "Biblio_Asig_03.h"

using namespace std;

int main(){
    int opcion;
    Fila fila;
    Pila pila;
    int codigo;

    do {
        cout << "Seleccione una opcion:" << endl;
        cout << "1. Fila" << endl;
        cout << "2. Pila" << endl;
        cout << "0. Salir" << endl;
        cin >> opcion;

        switch (opcion) {
            case 1:
                // Opciones para Fila
                do {
                    cout << "Seleccione una opcion para la Fila:" << endl;
                    cout << "1. Insertar nodo" << endl;
                    cout << "2. Eliminar nodo" << endl;
                    cout << "0. Regresar" << endl;
                    cin >> opcion;

                    switch (opcion) {
                        case 1:
                            cout << "Ingrese el codigo del nodo: ";
                            cin >> codigo;
                            fila.Insertar(codigo);
                            break;
                        case 2:
                            codigo = fila.Eliminar();
                            if (codigo == -1) {
                                cout << "La Fila esta vacia." << endl;
                            } else {
                                cout << "Se elimino el nodo con codigo: " << codigo << endl;
                            }
                            break;
                        case 0:
                            break;
                        default:
                            cout << "Opcion invalida." << endl;
                            break;
                    }
                } while (opcion != 0);
                break;
            case 2:
                // Opciones para Pila
                do {
                    cout << "Seleccione una opcion para la Pila:" << endl;
                    cout << "1. Insertar nodo" << endl;
                    cout << "2. Eliminar nodo" << endl;
                    cout << "0. Regresar" << endl;
                    cin >> opcion;

                    switch (opcion) {
                        case 1:
                            cout << "Ingrese el codigo del nodo: ";
                            cin >> codigo;
                            pila.Insertar(codigo);
                            break;
                        case 2:
                            codigo = pila.Eliminar();
                            if (codigo == -1) {
                                cout << "La Pila esta vacia." << endl;
                            } else {
                                cout << "Se elimino el nodo con codigo: " << codigo << endl;
                            }
                            break;
                        case 0:
                            break;
                        default:
                            cout << "Opcion invalida." << endl;
                            break;
                    }
                } while (opcion != 0);
                break;
            case 0:
                break;
            default:
                cout << "Opcion invalida." << endl;
                break;
        }
    } while (opcion != 0);

    return 0;
}