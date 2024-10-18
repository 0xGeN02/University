// Asignatura: TAyRE
// Prácticas de IoT
// Programa: IoTP04E03.ino 
// Placa Arduino Uno
// Sensor de Distancia HC-SR04
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        
// BIBLIOTECAS

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES 
   const int   Pin_Emitir  = 8;
   const int   Pin_Recibir = 9;
   // Velocidad del Sonido cm/seg
   const float V_Sonido    = 0.0343;
   const float HC_SR04_Max = 300; // Alcance máximo
   // Tiempo Espera Rebote Señal
   const long  Time_Out = 30000; 
   const int T_Pausa=2000;  // 2 segundos

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
   float HC_SR04(int, int);
   void Generar_Pulso(int);
   long Duracion_Eco(int);
   float Distancia(long);
   void Salida_Serial ( float  );

// BLOQUE DE INICIALIZACIÓN 
   void setup()
   {
    Serial.begin(9600); // Puerto Serial
    pinMode( Pin_Emitir  , OUTPUT );
    pinMode( Pin_Recibir , INPUT  );
    Salida_Serial ( 0.0 );
   }
// BLOQUE DE EJECUCIÓN
void loop()
{
 float D;
 D = HC_SR04(Pin_Emitir, Pin_Recibir);
 Salida_Serial(D);
 // Espera 2 segundos para tomar una nueva muestra
 delay(2000);
}
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS

// DECLARACIONES DE RUTINAS

// RUTINA Distancia TIPO: long
// Obtiene la distancia en función del tiempo de retorno 
// de la señal emitida por la sensor.
float Distancia( long Tiempo)
{
   return float(((Tiempo/2.0)*V_Sonido));
}
// RUTINA  HC_SR04 Tipo: Procedimiento
// Parámetros:
//    1. P_E     Tipo Entero Pin emitir
//    2. P_R     Tipo Entero Pin Recibir
// 
float HC_SR04(int P_E, int P_R)
{
   // Inicio del Pulso
 Generar_Pulso(P_E);
 return float(Distancia(Duracion_Eco(P_R)));
}

// Rutina de iniciar una medición.ir
void Generar_Pulso(int Pin)
{
  digitalWrite(Pin, LOW);  
  delayMicroseconds(5);
  digitalWrite( Pin, HIGH );
  delayMicroseconds(10); 
  digitalWrite( Pin, LOW );
}
//Rutina para calcular el tiempo de regreso  de la señal
long Duracion_Eco(int Pin)
{
  long T_Inicio = micros(); // Inicio
  long T_Eco = 0;
 // Espera Pin_Recibir cambie a HIGH
  while (digitalRead(Pin) == LOW) 
   if (micros() - T_Inicio > Time_Out) 
      return 0; // No se detecto ECO
  long T_Eco_R = micros(); 
 // Espera Pin_Recibir cambie a LOW
   while (digitalRead(Pin) == HIGH) 
   if (micros() - T_Inicio > Time_Out) 
      return 0; // Duración excesiva de ECO
  T_Eco = micros() - T_Eco_R;
return T_Eco;
}
//
// RUTINA: Salida_Serial
// Envía salida al puerto serial
void Salida_Serial ( float D)
{
if (D < HC_SR04_Max)
 {
    Serial.println("--------------------------");
    Serial.print(" Objeto a : ");
    Serial.print(D);
    Serial.println(" cm");
    Serial.println("--------------------------");
 }
 else
  Serial.println("No detectan objetos");
}
  