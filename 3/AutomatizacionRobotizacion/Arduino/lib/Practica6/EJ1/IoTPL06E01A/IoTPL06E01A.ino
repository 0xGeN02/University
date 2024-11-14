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
 	const int P_Led 		= 10; // Salida
 	const int P_Pulsador1  	=  2; // Entrada
 	const int P_Pulsador2  	=  5; // Entrada
// Variables
	int Estado; // Estado retornado por la Función de Transición de estado
    int EA; // Estado Actual
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_Transicion(int, int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
  // Iniciar Comunicación Serial
     Serial.begin(9600);   
  // Definición de Pines
  	  pinMode(P_Led,OUTPUT);
  	  pinMode(P_Pulsador1,INPUT);
  	  pinMode(P_Pulsador2,INPUT);
  // Estado Inicial
   	  Estado=0;EA=Estado;
	  digitalWrite(P_Led, LOW);
  // Serial Inicial
      Serial.print("Arduino A Estado : ");
      Serial.println(Estado); 
      Serial.print("Trasmitiendo Evento : " );
      Serial.println(' '); // Apagado
 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   Estado = F_Transicion(Estado, digitalRead(P_Pulsador1), digitalRead(P_Pulsador2));
   if (EA!=Estado)
   {
    Serial.print("Arduino A Estado : ");
    Serial.println(Estado); 
    Serial.print("Trasmitiendo a Arduino B Evento : " );
    Serial.println(Estado); // Encender 
    EA=Estado;             
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
int F_Transicion( int Edo, int P1, int P2)
{
 int E=Edo; 
 if ((Edo==0) && (P1==1))
 {
   digitalWrite(P_Led, HIGH);
   E=1;
 }
  else
   if ((Edo==1) && (P2==1))
   {
    digitalWrite(P_Led, LOW);
    E=0;
   }

 return E;
}
