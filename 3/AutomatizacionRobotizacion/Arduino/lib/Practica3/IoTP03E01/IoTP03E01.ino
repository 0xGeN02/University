
// Asignatura: TAyRE
// Programa: P03E01.ino   
// Placa Arduino Uno
// Entradas Analógicas
// Variables y Constantes.
// Potenciómetros
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        

// BIBLIOTECAS

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
// Pines DIGITALES del Aeduino
 	const int Pin_SD_Led = 7; // Salida Digital
    const int Pin_EA     = A0; // Entrada Analógica

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS

// BLOQUE INICIALIZACIÓN
   int valor=0;

 void setup()
 // Definición de Pines
 {
  pinMode(Pin_SD_Led, OUTPUT); 
  Serial.begin(9600); // Inicialización puerto Serial
 }
// BLOQUE EJECUCIÓN
void loop() 
{
  valor = analogRead(Pin_EA);
  Serial.println(valor);
  digitalWrite(Pin_SD_Led, HIGH); 
  delay(valor);                  
  digitalWrite(Pin_SD_Led, LOW);   
  delay(valor);   
}
// Fin Bloque Ejecución
