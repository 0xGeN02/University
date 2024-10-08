// Asignatura: TAyRE
// Programa: P02E01.ino   
// Placa Arduino Uno
// Entradas Digitales
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include <Arduino.h>
// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
// Pines DIGITALES del Aeduino
 	const int P_Led 		= 10; // Salida
 	const int P_Pulsador  	=  2; // Entrada
	int Estado;
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_Transicion(int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
  // Definición de Pines
  	pinMode(P_Led,OUTPUT);
  	pinMode(P_Pulsador,INPUT);
  // Estado Inicial
   	Estado=0;
	  digitalWrite(P_Led, LOW);
 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   Estado = F_Transicion(Estado, digitalRead(P_Pulsador));
 }
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS
//  Rutina: F_Transicion
/*  Función de transición de estados del modelo DES
	Parámetros: 
	Estado_Actual	Tipo: Entero Estado Actual del Sistema {0,1}
	Evento 			Tipo: Entero Pin asociado al pulsador
*/  	
int F_Transicion( int Edo, int Evento)
{
 int E=Edo; 
 if ((Edo==0) && (Evento==1))
 {
   digitalWrite(P_Led, HIGH);
   E=1;
 }
  else
   if ((Edo==1) && (Evento==0))
   {
    digitalWrite(P_Led, LOW);
    E=0;
   }

 return E;
}

