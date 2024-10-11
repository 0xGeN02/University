// Asignatura: TAyRE
// Programa: P02E03.ino   
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
	char Estado;
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_Transicion(int, int, int);
	void Muestra_Estado(char);

// BLOQUE INICIALIZACIÓN
void setup()
 {
   // Definición de Pines
  	pinMode(P_Led,OUTPUT);
    pinMode(P_Pulsador1,INPUT);
  	pinMode(P_Pulsador2,INPUT);
   // Iniciar el Puerto Serial
  	Serial.begin(9600); 
   // Estado Inicial
   	Estado='A';
	digitalWrite(P_Led, LOW);
    Muestra_Estado(Estado);
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
int F_Transicion( char Edo, int P1, int P2)
{
 char E=Edo; 
 if ((Edo=='A') && (P1==1))
 {
   digitalWrite(P_Led, HIGH);
   E='E';
   Muestra_Estado(E);
 }
  else
   if ((E=='E') && (P2==1))
   {
    digitalWrite(P_Led, LOW);
    E='A';
    Muestra_Estado(E); 
   }
 return E;
}

// Rutina Muestra Estado en Terminal
void Muestra_Estado(char E)
{
 Serial.print("Estado : ");
 Serial.println(E); 
}
