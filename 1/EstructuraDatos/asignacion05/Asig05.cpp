//RUTINA DE SOPORTE PARA GENERAR NÚMEROS ENTEROS
#include "Asig.05.h"

Arbol_B::Arbol_B() : raiz(nullptr) {}

Arbol_B::~Arbol_B(){
    // TODO: Implementar destructor
}
void Arbol_B::insertar(int valor){

}

bool Arbol_B::buscar(int valor) const{

}

void NUM_ALEA_P4(vector<int>& Vec, int N, int LI, int LS, unsigned semilla ){
 Vec.clear();
 Vec.push_back(50); Vec.push_back(25); Vec.push_back(75);
 // Verifica si es posible generar N enteros distintos en el rango [LI, LS]
 if (N > LS - LI + 1) 
 {
  cerr << "No es posible generar " << N << " enteros distintos en el rango [" << LI << "," << LS << "].\n";
  return;
 }
// Genera los números aleatorios no repetidos
 mt19937 generator(semilla);
 uniform_int_distribution<int> distribution(LI, LS);
 while (Vec.size() < (unsigned)N) 
 {
  int numero = distribution(generator);
  if (find(Vec.begin(), Vec.end(), numero) == Vec.end()) 
  {
   Vec.push_back(numero);
  }
 }
  Vec.push_back(1); Vec.push_back(99); 
}