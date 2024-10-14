// Asignatura: TAyRE
// Programa: P02E03.ino   
// Placa Arduino Uno
// Entradas Digitales. Dos Pulsadores
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
#include "IoT_P02_E04.h"
// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES
const int P_Led1 = 5;  // Pin del LED 1
const int P_Led2 = 7;  // Pin del LED 2
const int P_Led3 = 9;  // Pin del LED 3
const int P_Led4 = 11; // Pin del LED 4
const int P_Led5 = 13; // Pin del LED 5
const int P_Pulsador1 = 2; // Pin del pulsador +
const int P_Pulsador2 = 3; // Pin del pulsador -

int numLedsEncendidos = 0;  // Contador de LEDs encendidos
bool estadoAnteriorPulsador1 = LOW;  // Estado anterior del pulsador +
bool estadoAnteriorPulsador2 = LOW;  // Estado anterior del pulsador -

// BLOQUE INICIALIZACIÓN
void setup_P02E04() {
  // Definición de Pines
  pinMode(P_Led1, OUTPUT);
  pinMode(P_Led2, OUTPUT);
  pinMode(P_Led3, OUTPUT);
  pinMode(P_Led4, OUTPUT);
  pinMode(P_Led5, OUTPUT);
  pinMode(P_Pulsador1, INPUT);
  pinMode(P_Pulsador2, INPUT);

  // Iniciar el Puerto Serial
  Serial.begin(9600);

  // Estado Inicial (todos los LEDs apagados)
  apagaTodosLeds(); // lama al método para apagar todos los Leds y aquí se crea la variable numLedsEncendidos
  Serial.println("Estado inicial: Todos los LEDs apagados");  // Que lo imprima en la terminal
}

// BLOQUE EJECUCIÓN
void loop_P02E04() {
  // Leer estado de los pulsadores
  bool estadoPulsador1 = digitalRead(P_Pulsador1);
  bool estadoPulsador2 = digitalRead(P_Pulsador2);

  // Pulsador + (incrementa LEDs encendidos)
  if (estadoPulsador1 == HIGH && estadoAnteriorPulsador1 == LOW) {  // si el pulsador1 se enciende y antes estaba apagado, es para que si se le da dos veces seguidas al pulsador, no haga nada
    if (numLedsEncendidos < 5) {  // si hay menos de 5 Leds encendidos, porque solo hay 5 Leds y no se pueden encender más
      numLedsEncendidos++;  // aumenta en uno la variable numLedsEncendidos
      actualizaLeds();  // llama al método actualizaLeds que es el que enciende el led
    }
    Serial.print("Pulsador +: ");
    Serial.println(numLedsEncendidos);  // Imprime la cantidad de Leds encendidos
  }

  // Pulsador - (decrementa LEDs encendidos)
  if (estadoPulsador2 == HIGH && estadoAnteriorPulsador2 == LOW) { // si el pulsador2 se enciende y antes estaba apagado
    if (numLedsEncendidos > 0) {  // si no hay Leds encendidos
      numLedsEncendidos--;  // Se disminuye en uno la variable numLedsEncendidos
      actualizaLeds();  // Se llama al método para que apague el led
    }
    Serial.print("Pulsador -: ");
    Serial.println(numLedsEncendidos);  // Imprime la variable
  }

  // Actualizar los estados anteriores de los pulsadores
  estadoAnteriorPulsador1 = estadoPulsador1;  // El estado al que pasó el pulsador1 pasa a ser el estado anterior para que luego, en los if del loop para que no cambie de estado ni haga nada si se pulsa un boton 2 veces seguidas. Es decir, si estadoPulsador1 == estadoAnteriorPulsador1
  estadoAnteriorPulsador2 = estadoPulsador2;

  delay(100);  // Pequeño retardo para evitar rebotes
}

// Función que enciende/apaga los LEDs según el número de LEDs encendidos
// Si la variable actualizada
void actualizaLeds() {
  // La ? es un operador condicional que dependiendo de un suceso, realizo un suceso u otro
  digitalWrite(P_Led1, (numLedsEncendidos >= 1) ? HIGH : LOW);  // Dependiendo de si la variable numLedsEncendidos es mayor o igual a 1, enciende o apaga el Led. Si es mayor enciende el Led y si es menor lo apaga
  digitalWrite(P_Led2, (numLedsEncendidos >= 2) ? HIGH : LOW);
  digitalWrite(P_Led3, (numLedsEncendidos >= 3) ? HIGH : LOW);
  digitalWrite(P_Led4, (numLedsEncendidos >= 4) ? HIGH : LOW);  // Si por ejemplo, la variable de numLedsEncendidos es 4, enciende el 1, 2, 3 y 4 porque son mayores o iguales a 4. Y como 5 es mayor que 4, se apaga
  digitalWrite(P_Led5, (numLedsEncendidos >= 5) ? HIGH : LOW);
}

// Función que apaga todos los LEDs. Se crea este método porque es el estado inicial
void apagaTodosLeds() {
  digitalWrite(P_Led1, LOW);
  digitalWrite(P_Led2, LOW);
  digitalWrite(P_Led3, LOW);
  digitalWrite(P_Led4, LOW);
  digitalWrite(P_Led5, LOW);
  numLedsEncendidos = 0;  // Crea la variable de el número de Leds encendidos, como todos están apagados, la variable es igual a 0
}