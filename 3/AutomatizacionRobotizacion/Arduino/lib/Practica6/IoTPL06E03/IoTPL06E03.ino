// Asignatura: TAyRE
// Programa: IoTPL06E03.ino
// Placa Arduino Uno
// Comunicación Bluetooth
// Configuración Módulo Bluetooth
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include <SoftwareSerial.h>
// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
int Rx = 10; //Conexion Recepción Serie 
int Tx = 11; //Conexión Transmisión Serie
// Variables
SoftwareSerial moduloBtLE(Rx,Tx); //Objeto para el manejo de conexion Serie
int baudRateSerial = 9600; // Velocidad de transmisión PC/HM-10 a través USB
int baudRateBLE = 9600;   // Velocidad de transmisión bluetooth

// BLOQUE INICIALIZACIÓN
void setup(){
  // Iniciar Comunicación Serial
  Serial.begin(baudRateSerial);
  while (!Serial) {
    }// espera conexión
  Serial.println("\n USB <->PC, Listo..!!");
  
  // Iniciar Comunicación Serial con módulo Bluetooth
  moduloBtLE.begin(baudRateBLE);
  moduloBtLE.println("Listo Bluetooth a Tablet/móvil");
  delay(1000);
}

// BLOQUE EJECUCIÓN
void loop(){
  // recibe mensaje Bluetooth y envia por USB a PC
  if (moduloBtLE.available()){
    Serial.write(moduloBtLE.read());
    }
  // envia mensaje Serial-USB a Bluetooth
  if (Serial.available()){
    moduloBtLE.write(Serial.read());
    }
  }
