// Asignatura: TAyRE
// Programa: IoTP05E03.ino
// Placa Arduino Uno
// servomotor 
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        
// INCLUSIÓN DE BIBLIOTECAS
   #include <Servo.h>
// PROTOTIPOS DE RUTINAS
   void Motor_Angulo( int );
   void Mover_Motor( );

// DECLARACIONES Y DEFINICIONES
// CONSTANTES
   const int Pin_Servo = 7;
   const int Pausa = 2000; // 2 segundo
   const int Inc   =30; // Incrementos de 30 grados
// VARIABLES
   Servo Motor_01;
// BLOQUE DE INICIALIZACIÓN 
void setup()
{
  // Pin asociado al Motor_01
   Motor_01.attach(Pin_Servo);
  // Puerto Serial 
   Serial.begin(9600);
   Motor_01.write(0);
}

void loop() 
{
 Mover_Motor( );
}
// DELACRACIONES DE RUTINAS

// Motor Ángulo
// Envia al pruerto serial la posición del servo
// Parámetro: a Tipo: Entero   Ángulo del servo
void Motor_Angulo(int a)
{
   Serial.print("Motor en: ");
   Serial.println(a);  
}
// Mover_Motor
// Movimiento del servo

void Mover_Motor( )
{
  int m;
  for (m=0;m<=180;m=m+Inc)
  {
   Motor_01.write(m);
   Motor_Angulo(Motor_01.read());
   delay(Pausa); 
  }
}
