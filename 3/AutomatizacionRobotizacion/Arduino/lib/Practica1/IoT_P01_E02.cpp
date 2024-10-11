// Asignatura: TAyRE
// Programa: P01E02.ino   
// Iniciación con Placa Arduino Uno
// Simular un semaforo
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include "IoT_P01_E02.h"

// DEFINICIÓN DE VARIABLES Y CONSTANTES
	const int Pin_V =3;	 // Pin conectado a verde
	const int Pin_A =5;	 // Pin conectado a amarillo
	const int Pin_R =7;	 // Pin conectado a Rojo
 	const int tv=3;      // Evento tiempo en verde    segundos
 	const int ta=2;      // Evento tiempo en amarillo segundos
 	const int tr=3;      // Evento tiempo en rojo     segundos
 	char  Estado_Actual; // Estado del Sistema
 	int   Next_t=0;			   // Próximo tiempo de permanencia en el estado actual

// BLOQUE INICIALIZACIÓN
void setupIoTP01E02() 
{  
 // Incialización de los Pines Digitales del Arduino Uno
  pinMode(Pin_V, OUTPUT);  	 // Pin asociado al led Verde  
  pinMode(Pin_A, OUTPUT);  	 // Pin asociado al led Amarillo           
  pinMode(Pin_R, OUTPUT);  	 // Pin asociado al led Rojo
 // Estado Inicial
  digitalWrite(Pin_V, LOW);  // Verde    OFF Inicial
  digitalWrite(Pin_A, LOW);  // Amarillo OFF Inicial
  digitalWrite(Pin_R, LOW);  // Rojo     OFF Inicial
}
// FIN BLOQUE INICIALIZACIÓN

// BLOQUE EJECUCIÓN
void loopIoTP01E02() {
 // DECLARACION DE VARIABLES LOCALES
  switch (Estado_Actual){
    case 'V':
      E_Verde();
      break;
    
    case 'A':
      E_Amarillo();
      break;
    
    case 'R':
      E_Rojo();
      break;
  }

 // FUNCIÓN DE TRANSICIÓN DE ESTADO
  Estado_Actual=F_Transicion(Estado_Actual,Next_t, Pin_V,tv,Pin_A,ta,Pin_R,tr);
      
}
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS

//  Rutina: F_Transicion
/*  Función de transición de estados del modelo DES
	Parámetros: 
	Estado_Actual		Tipo: char 	 Estado Actual del Sistema {'V', 'A', 'R'}
	Pin_V, Pin_A, Pin_R	Tipo: Entero Pines conectados a cada Led
  	TV, TR, TA			Tipo: Entero Tiempo de permanencia en cada estado
*/
char F_Transicion( char X, int t, int PV, int TV, int PA, int TA, int PR, int TR){
  char E;
  delay(t*1000);
  if (X=='V'){
    Next_t=TA;
    E='A';
    E_Amarillo();
  }
  else{
    if (X=='A'){
      Next_t=TR;
      E='R';
      E_Rojo();
    } 
    else{
      Next_t=TV;
      E='V';
      E_Verde();
    }
  }
  return E;
}

// Rutina: E_Verde
/* Parámetros: NO
	  Acciones de Transición del Estado (Verde)
	  Tipo: Entero Tiempo de permanencia en cada estado
*/
void E_Verde(){
  digitalWrite(Pin_R, LOW);
  digitalWrite(Pin_V, HIGH);  
}

// Rutina: E_Amarillo
/* Parámetros: NO
	  Acciones de Transición del Estado (Amarillo)
	  Tipo: Entero Tiempo de permanencia en cada estado
*/
void E_Amarillo(){
  digitalWrite(Pin_V, LOW);
  digitalWrite(Pin_A, HIGH);  
}

// Rutina: E_Rojo
/* Parámetros: NO
	  Acciones de Transición del Estado (Rojo)
	  Tipo: Entero Tiempo de permanencia en cada estado
*/
void E_Rojo(){
  digitalWrite(Pin_A, LOW);
  digitalWrite(Pin_R, HIGH);  
}