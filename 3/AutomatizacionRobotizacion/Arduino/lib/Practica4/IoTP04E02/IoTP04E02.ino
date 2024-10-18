// Asignatura: TAyRE
// Prácticas de IoT
// Programa: IoTP04E02.ino 
// Placa Arduino Uno
// Sensor Photosensitive
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 18/08/2024        
// BIBLIOTECAS

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES 
   const int Pin_Sensor  = A0;       // Pin Fotodiodo
   const int Pin_Led = 8;            // Pin Led
   const int Umbral_Encender = 512;  // Valor para encender

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
   void Encender_Led(int, int, int); // Determina si se enciende el Led

// BLOQUE DE INICIALIZACIÓN 
void setup() 
{
  pinMode(Pin_Led, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(9600);       // Inicia la comunicación serial
}
// BLOQUE DE EJECUCIÓN
void loop() 
{
 // Leer Entrada Analógica
  int Lectura = analogRead(Pin_Sensor); 
  Encender_Led(Pin_Led, Umbral_Encender, Lectura);
  Serial.print("Entrada A0 : ");
  Serial.println(Lectura);
  // Esperar 1 seg
  delay(1000); 
}
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS
// RUTINA  Encender-Led Tipo: Procedimiento
// Parámetros:
//    1. Pin     Tipo Entero Pin de conexión del Led
//    2. Umbral  Tipo Entero Valor de Encendido
//    3. Valor   Timpo Entero Valor de la lectura 
void Encender_Led(int Pin, int Umbral, int Valor)
{
 if (Valor > Umbral)
  digitalWrite(Pin,HIGH);
 else
  digitalWrite(Pin,LOW);
}
