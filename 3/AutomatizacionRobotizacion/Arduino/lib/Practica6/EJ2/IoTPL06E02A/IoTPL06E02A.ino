// Asignatura: TAyRE
// Programa: IoTPL06E01A.ino  //ARDUINO A   
// Placa Arduino Uno
// Comunicación Serial
// Botones Encender / Apagar
// Estados Sistema X={E,A} ={1,0}
// Eventos Sistema E={e,a} = {1,0} -> 1=Pin 2 y 0=Pin 5  (Pines asociados)
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
// Pines DIGITALES del Aeduino
 	const int P_Led1 		= 10; // Salida
  const int P_Led2     = 3;  //Salida
 	const int P_Pulsador1  	=  2; // Entrada
// Variables
	int Estado; // Estado retornado por la Función de Transición de estado
  int EA; // Estado Actual
	int lectura;
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_Transicion(int, int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
  // Iniciar Comunicación Serial
     Serial.begin(9600);   
  // Definición de Pines
  	  pinMode(P_Led1,OUTPUT);
      pinMode(P_Led2,OUTPUT);
  	  pinMode(P_Pulsador1,INPUT);
  // Estado Inicial
   	  Estado=0;EA=Estado;
	  digitalWrite(P_Led1, LOW);
    digitalWrite(P_Led2, HIGH);
  // Serial Inicial
      Serial.print("Arduino A Estado : ");
      Serial.println(Estado); 
      Serial.print("Trasmitiendo Evento : " );
      Serial.println(' '); // Apagado
  	lectura = 1;
 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   // Actualizar el estado
   Estado = F_Transicion(Estado, digitalRead(P_Pulsador1), lectura);
   if (EA!=Estado)
   {
    Serial.print("Arduino A Estado : ");
    Serial.println(Estado); 
    Serial.print("Trasmitiendo a Arduino B Evento : " );
    Serial.println(Estado); // Encender 
    EA=Estado;             
   }
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
	Evento 			Tipo: Entero Pin asociado al pulsador
*/  	
int F_Transicion( int Edo, int P1, int e)
{
 int E=Edo; 
 if ((Edo==0) && (P1==1))
 {
   digitalWrite(P_Led1, HIGH);
   digitalWrite(P_Led2, LOW);

   E=1;
 }
  else    // Cambiar esto
   if ((Edo==1) && (e=='0'))
   {
    digitalWrite(P_Led1, LOW);
    digitalWrite(P_Led2, HIGH);
    E=0;
   }

 return E;
}