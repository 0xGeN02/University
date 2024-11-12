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
 	const int P_Led 		= 10; // Salida

// Variables
	int EstadoB; // Estado retornado por la Función de Transición de estado
// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
	int F_TransicionB(int, int, int);

// BLOQUE INICIALIZACIÓN
void setup()
 {
  // Iniciar Comunicación Serial
     Serial.begin(9600);   
  // Definición de Pines
  	  pinMode(P_Led,OUTPUT);
  // Estado Inicial
   	  EstadoB=0;
	  digitalWrite(P_Led, LOW);
      Serial.print("Arduino B Estado : ");
      Serial.println(EstadoB); 
  // Serial Inicial

 }
// BLOQUE EJECUCIÓN
 void loop()
 {
   if (Serial.available()) 
   {  
     EstadoB = F_Transicion(EstadoB, Serial.read());
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
 int E=Edo; 
 if ((Edo==0) && (e=='1'))
 {
   digitalWrite(P_Led, HIGH);
   E=1;
   Serial.print("Arduino B Estado : ");
   Serial.println(E);
 }
  else
   if ((Edo==1) && (e=='0'))
   {
    digitalWrite(P_Led, LOW);
    E=0;
    Serial.print("Arduino B Estado : ");
    Serial.println(E);
   }

 return E;
}
