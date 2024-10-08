// Asignatura: TAyRE
// Programa: P02E02.ino   
// Placa Arduino Uno
// Entradas Digitales. Dos Pulsadores
// Estados X={A,E}
// Eventos E={a1,c2} -> a1=2 y C2=5  (Pines asociados)
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include <Arduino.h>
// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
// Pines DIGITALES del Aeduino
 	const int P_Led 		= 10; // Salida
 	const int P_Pulsador1  	=  2; // Entrada
 	const int P_Pulsador2  	=  5; // Entrada
	int Estado;
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_Transicion(int, int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
  // Definición de Pines
  	  pinMode(P_Led,OUTPUT);
  	  pinMode(P_Pulsador1,INPUT);
  	  pinMode(P_Pulsador2,INPUT);
  // Estado Inicial
   	  Estado=0;
	  digitalWrite(P_Led, LOW);
 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   Estado = F_Transicion(Estado, digitalRead(P_Pulsador1), digitalRead(P_Pulsador2));
 }
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS
//  Rutina: F_Transicion
/*  Función de transición de estados del modelo DES
	Parámetros: 
	Estado_Actual	Tipo: Entero Estado Actual del Sistema {0,1}
	Evento 			Tipo: Entero Pin asociado al pulsador
*/  	
int F_Transicion( int Edo, int P1, int P2)
{
 int E=Edo; 
 if ((Edo==0) && (P1==1))
 {
   digitalWrite(P_Led, HIGH);
   E=1;
 }
  else
   if ((Edo==1) && (P2==1))
   {
    digitalWrite(P_Led, LOW);
    E=0;
   }

 return E;
}
