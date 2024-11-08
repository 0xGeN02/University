// Asignatura: TAyRE
// Programa: IoTP05E02.ino
// Control de velocidad de un Motor DC
// Modulación de Pulso PWM
// Placa Arduino Uno, Integrado L293D, Motor DC 
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        
// INCLUSIÓN DE BIBLIOTECAS

// PROTOTIPOS DE RUTINAS

    void MotorControlVelocidad(int , int , int , int );
    void Motor_OFF    (int, int, int);

// DECLARACIONES Y DEFINICIONES
// CONSTANTES
// PINES ASOCIADOS AL INTEGRADO L293D
   const int   MIN_PWM   =   0;
   const int   MAX_PWM   = 255; //Máximo valor de modulación
   const int   Activar   =  11;
   const int   Entrada_1 =  10;
   const int   Entrada_2 =  9;
// BLOQUE DE INICIALIZACIÓN 
   void setup()
   {
    // Pines de Salida L293D 
    pinMode( Activar   , OUTPUT );
    pinMode( Entrada_1 , OUTPUT );
    pinMode( Entrada_2 , OUTPUT );
    // Puerto Serial 
    Serial.begin(9600);
    // Estado Inicial Motor Apagado
    Motor_OFF    (Activar, Entrada_1, Entrada_2); 
   }
// BLOQUE DE EJECUCIÓN
void loop()
{
  int r;
  for (r=4;r>0;r=r-1) // Velocidades [25%, 33%, 50%, 100%] 
  {
    // Activar motor DC velocidad 25%
  	MotorControlVelocidad(Activar, Entrada_1, Entrada_2, int(MAX_PWM/r));
    Serial.print("Motor: Girando % : ");
    Serial.println(int(100/r));
	delay(2000); 
   // Apagar motor DC
    Motor_OFF(Activar, Entrada_1, Entrada_2);
   	delay(1000);
  } 
}
// DELACRACIONES DE RUTINAS

// Rutina:  MotorControlVelocidad
// Activa el motor con giro a la derecha o izquierda
// Parámetros:
// E  Tipo: Entero Pin de Activación del Integrado L293D
// E1 Tipo: Entero Pin de Entrada 1 del Integrado L293D
// E2 Tipo: Entero Pin de Entrada 2 del Integrado L293D
// D  Tipo: Entero Velocidad PWM
void MotorControlVelocidad(int E, int E1, int E2, int D) 
{
 // Activar motor y ajustar velocidad 
 digitalWrite(E1, LOW);
 digitalWrite(E2, HIGH);
 analogWrite(E, D); // El pulso de activación PWN es analógico
// 
}

// Rutina:  Motor_OFF 
// Apaga el motor DC
// Parámetros:
// E  Tipo: Entero Pin de Activación del Integrado L293D
// E1 Tipo: Entero Pin de Entrada 1 del Integrado L293D
// E2 Tipo: Entero Pin de Entrada 2 del Integrado L293D

void Motor_OFF (int E, int E1, int E2)
{
 analogWrite(E, LOW);
 digitalWrite(E1, LOW);
 Serial.println("Motor: Girando % : 0");
}
