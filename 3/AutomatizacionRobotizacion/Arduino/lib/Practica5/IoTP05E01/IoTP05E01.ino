// Asignatura: TAyRE
// Programa: IoTP05E01.ino
// Encender y Apagar un Motor DC y Sentido de Giro
// Placa Arduino Uno, Integrado L293D, Motor DC 
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        
// INCLUSIÓN DE BIBLIOTECAS

// PROTOTIPOS DE RUTINAS

    void MotorControl(int , int , int , int );
    void Motor_OFF    (int, int, int);

// DECLARACIONES Y DEFINICIONES
// CONSTANTES
// PINES ASOCIADOS AL INTEGRADO L293D
   const int   Activar   =  11;
   const int   Entrada_1 =  10;
   const int   Entrada_2 =   9;
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
   // Activar motor DC girando en a la Izquierda
  	MotorControl(Activar, Entrada_1, Entrada_2, 0);
    Serial.println("Motor: Girando Izquierda");
	delay(2000); 
   // Apagar motor DC
    Motor_OFF(Activar, Entrada_1, Entrada_2);
    Serial.println("Motor: Apagado");
 	delay(1000);
   // Activar motor DC girando en a la Derecha
    MotorControl(Activar, Entrada_1, Entrada_2, 1);
	delay(2000); 
    Serial.println("Motor: Girando Derecha");
   // Apagar motor DC
    Motor_OFF(Activar, Entrada_1, Entrada_2);
    Serial.println("Motor: Apagado");
	delay(1000);
}
// DELACRACIONES DE RUTINAS

// Rutina:  MotorControl
// Activa el motor con giro a la derecha o izquierda
// Parámetros:
// E  Tipo: Entero Pin de Activación del Integrado L293D
// E1 Tipo: Entero Pin de Entrada 1 del Integrado L293D
// E2 Tipo: Entero Pin de Entrada 2 del Integrado L293D
// D  Tipo: Entero Sentido de Giro 0 Izquierda 1 Derecha
void MotorControl(int E, int E1, int E2, int D) 
{
 // Activar motor y ajustar velocidad 
 analogWrite(E, HIGH);
 if (D==0)
 {
    digitalWrite(E, HIGH);
	digitalWrite(E1, HIGH);
	digitalWrite(E2, LOW);
 }
 else
 {
    digitalWrite(E, HIGH);   
	digitalWrite(E1, LOW);
	digitalWrite(E2, HIGH);
 }
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
 digitalWrite(E, LOW);
 digitalWrite(E1, LOW);
 digitalWrite(E2, LOW);
}
