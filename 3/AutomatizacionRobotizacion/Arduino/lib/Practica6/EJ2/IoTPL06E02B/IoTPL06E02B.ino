// Asignatura: TAyRE
// Programa: IoTPL06E01B.ino  //ARDUINO B   
// Placa Arduino Uno
// Comunicación Serial
// Led Encender / Apagar Según Indicación de Arduino A
// Estados Sistema X={E,A} ={1,0}
// Eventos Sistema E={e,a} = {1,0}
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
// Pines DIGITALES del Aeduino
// PINES ASOCIADOS AL INTEGRADO L293D
  const int   Activar   =  11;
  const int   Entrada_1 =  10;
  const int   Entrada_2 =   9;

// Variables
  const unsigned long T = 5000;
	int lectura = 0;
// Variables de estado
	int EstadoB; // Estado retornado por la Función de Transición de estado
  unsigned long inicioTiempoMotor = 0;

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_TransicionB(int, int);
  void MotorControl(int , int , int , int );
  void Motor_OFF    (int, int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
    // Pines de Salida L293D 
    pinMode( Activar   , OUTPUT );
    pinMode( Entrada_1 , OUTPUT );
    pinMode( Entrada_2 , OUTPUT );
  // Iniciar Comunicación Serial
     Serial.begin(9600);   
  // Estado Inicial
   	  EstadoB=0;
	  Motor_OFF    (Activar, Entrada_1, Entrada_2);
      Serial.print("Arduino B Estado : ");
      Serial.println(EstadoB); 
      lectura = 0;
  // Serial Inicial

 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   EstadoB = F_Transicion(EstadoB, lectura);
   if (Serial.available()) 
   {  
     lectura = Serial.read();
   }
 }
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS
//  Rutina: F_Transicion
/*  Función de transición de estados del modelo DES
	Parámetros: 
	Estado_Actual	Tipo: Entero Estado Actual del Sistema {0,1}
	Evento 			Tipo: Cracter Lectura Serial
*/  	
int F_Transicion( int Edo, int e)
{
 static bool temporizador_activo = 0;
 int E=Edo; 
 if ((Edo==0) && (e=='1'))
 {
    inicioTiempoMotor = millis();
    temporizador_activo = 1;
   // Activar motor DC girando en a la Izquierda
  	MotorControl(Activar, Entrada_1, Entrada_2, 0);
   E=1;
 }

  if ((temporizador_activo == 1))
  {
    if (millis() - inicioTiempoMotor >= T) {
    // Apagar motor DC
      Motor_OFF(Activar, Entrada_1, Entrada_2);
      E=0;
      Serial.print("Arduino B Estado : ");
      Serial.println(E);
      Serial.print("Trasmitiendo a Arduino A Evento : " );
      Serial.println(E); // Encender 
      temporizador_activo = 0;
      EstadoB=E;
    }
  }

 return E;
}

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