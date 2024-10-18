// Asignatura: TAyRE
// Programa: IoTP03E04.ino con LCD integrado
// Placa Arduino Uno
// Potenciometro, Secuencia de Leds, Estado y Pantalla LCD
// Programa de uso académico
// Realizado por: xGeN02
// Fecha: 18/10/2024

// BIBLIOTECAS
#include <LiquidCrystal.h>  // Biblioteca para la pantalla LCD

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES  
const int Total_Pines = 5;  // Cantidad de LEDs conectados a pines digitales consecutivos
const int Pin_Analog = A0;  // Pin analógico del potenciómetro
int Umbral[Total_Pines] = {170, 340, 510, 680, 850}; // Umbrales para los eventos de estado
int Pin_I = 6;  // Inicio de conexiones de LEDs
int Estado = 0;  // Estado inicial del sistema
int EA = 0;  // Última lectura del pin analógico

// LCD conectado a los pines digitales 12, 11, 5, 4, 3, 2
LiquidCrystal LCD1(12, 11, 5, 4, 3, 2);

// PROTOTIPOS DE FUNCIONES
void Inicializar_Pines(int, int);       // Definición de pines de salida
int F_Transision_Estados(int, int, int[]); // Función para la transición de estados
void Encender(int);                     // Enciende LEDs según el estado
void Salida_Serial(int, int);           // Muestra el estado en el puerto Serial
void Mostrar_LCD(int, int);             // Muestra el estado en la pantalla LCD

// BLOQUE DE INICIALIZACIÓN
void setup() 
{
  Inicializar_Pines(Pin_I, Total_Pines); // Inicializa los pines para los LEDs
  Serial.begin(9600);                    // Inicialización del puerto Serial
  LCD1.begin(16, 2);                     // Inicialización del LCD (16x2)
  
  Salida_Serial(Estado, 0);              // Muestra el estado inicial
  Mostrar_LCD(Estado, 0);                // Muestra en la pantalla LCD el estado inicial
  Encender(0);                           // Enciende el LED inicial
}

// BLOQUE DE EJECUCIÓN
void loop() 
{
  int Evento = analogRead(Pin_Analog);   // Lee el valor del potenciómetro
  Estado = F_Transision_Estados(Estado, Evento, Umbral); // Transición de estados según la entrada analógica
  
  if (EA != Evento)                      // Si el valor de la entrada cambia
  {
    Encender(Estado);                    // Actualiza los LEDs según el estado
    Salida_Serial(Estado, Evento);       // Muestra el estado en el puerto Serial
    Mostrar_LCD(Estado, Evento);         // Muestra el estado en la pantalla LCD
    EA = Evento;                         // Actualiza el valor de la última lectura
  }
}

// DECLARACIONES DE FUNCIONES

// Función para inicializar los pines del Arduino
void Inicializar_Pines(int P_I, int T)
{
  for (int i = 0; i <= (T - 1); i++)
  {
    pinMode((i + P_I), OUTPUT); // Configura los pines de los LEDs como salida
  }
}

// Función para gestionar la transición de estados
int F_Transision_Estados(int Edo, int Evento, int u[])
{
  int k = 0;
  while ((k <= Total_Pines - 1) && (u[k] < Evento))
  {
    k = k + 1;
  }
  return k;
}

// Función para encender y apagar los LEDs según el estado
void Encender(int a)
{
  for (int k = 0; k < a; k++)
  {
    digitalWrite(k + Pin_I, HIGH); // Enciende los LEDs hasta el estado actual
  }
  for (int k = a; k <= Total_Pines; k++)
  {
    digitalWrite(k + Pin_I, LOW);  // Apaga los LEDs por encima del estado actual
  }
}

// Función para mostrar el estado y la entrada en el puerto Serial
void Salida_Serial(int E, int ev)
{
  Serial.println("-----------------------------------");
  Serial.print("    ESTADO : "); Serial.print(E);
  Serial.print("    ENTRADA : "); Serial.println(ev);
  Serial.println("-----------------------------------");
}

// Función para mostrar el estado y la entrada en la pantalla LCD
void Mostrar_LCD(int E, int ev)
{
  LCD1.clear();                    // Limpia la pantalla
  LCD1.setCursor(0, 0);            // Posiciona el cursor en la primera línea
  LCD1.print("Estado: ");           // Muestra el texto "Estado: "
  LCD1.print(E);                    // Muestra el estado actual
  LCD1.setCursor(0, 1);             // Posiciona el cursor en la segunda línea
  LCD1.print("Entrada: ");          // Muestra el texto "Entrada: "
  LCD1.print(ev);                   // Muestra el valor de la entrada analógica
}
