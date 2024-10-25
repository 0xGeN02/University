// Asignatura: TAyRE
// Prácticas de IoT
// Programa: IoTP04E04.ino   
// Placa Arduino Uno
// Potenciometro, Secuencia de Leds y Estado
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include <Arduino.h> // Biblioteca de Arduino

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES  
   const int Total_Pines         = 5;  // Cantidad de Leds Conectado a pines Digitales consecutivos
   const int Pin_Analog = A0;
   int       Umbral[Total_Pines] = {170,340,510,680,850}; // Umbrales de valores de Eventos aceptados
   int       Pin_I               = 6;   // Inicio de conexiones de Leds
   int       Estado              = 0;   // Estado del Sistema {0, 1, 2, 3, 4 ,5 }Inicial 0)
   int       EA                  = 0;   // Lectura del Pin Anaógico

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
   void Inicializar_Pines ( int, int );         // Definición de Pines
   int  F_Transision_Estados(int, int, int []); // Transición de Estados (Estado, Evento, Umbrales)
   void Encender(int);                          // Enciende Leds según el estado
   void Salida_Serial(int, int);

// BLOQUE INICIALIZACIÓN

   void setup() 
   {
    Inicializar_Pines (Pin_I, Total_Pines);
    Serial.begin( 9600 ); // Inicialización puerto Serial
    Salida_Serial(Estado, 0); // Muestra Inicial
    Encender(0);
   }

// BLOQUE EJECUCIÓN

void loop() 
{
 int Evento;   // Variable que recibe el valor de la función analogRead()
 Evento = analogRead(Pin_Analog);
 Estado = F_Transision_Estados(Estado, Evento, Umbral);
 if (EA!=Evento)
 {
  Encender(Estado);
  Salida_Serial(Estado,Evento);
  EA=Evento;
 }
}
// FIN BLOQUE EJECUCIÓN
// DECLARACIONES DE RUTINAS
// Inicializar Pines del Arduino
void Inicializar_Pines(int P_I, int T)
{
  int i;
  for (i=0;i<=(T-1);i++)
   pinMode((i+P_I),  OUTPUT ); // Pin Digital de Salida
}
// FUNCIÓN DE TRANSICIÓN DE ESTADOS
// Tipo: Entero Nombre: F_Transision_Estados
// PARÁMETROS:
//      int Edo      Estado del Sistema
//      int Evento   Evento actual
//      Areeglo Enteros con los umbrales de cambio de estado del sistema
// Retorna E    Estado del sistema 

int F_Transision_Estados(int Edo, int Evento , int u[])
{
 int k;
 k=0;
 while ( (k<=Total_Pines-1)&&(u[k]<Evento))
 {
  k=k+1;
 }
 return k;
}
// Encender y Apagar Leds según el Estado del Sistema
void Encender( int a)
{
 int k=0;
 while ((k<a)&&(k<=Total_Pines))
 {
  digitalWrite(k+Pin_I, HIGH);
  k=k+1; 
 }
 k=a;
 while (k<=Total_Pines)
 {
  digitalWrite(k+Pin_I, LOW);
  k=k+1; 
 }
}

void Salida_Serial(int E, int ev) // Muestra Inicial
{
 Serial.println  ( "-----------------------------------" ); 
 Serial.print    ( "    ESTADO : " ); Serial.print( E );
 Serial.print    ( "    ENTRADA : " );Serial.println( ev );
 Serial.println  ( "-----------------------------------" ); 
}