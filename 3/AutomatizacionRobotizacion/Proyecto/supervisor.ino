#include <Arduino.h>

// Definición de pines
const int salida_E01 = 2;
const int salida_E02 = 3;
const int digito_R_1 = 4;
const int digito_R_2 = 5;
const int digito_R_3 = 6;
const int digito_E01_1 = 7;
const int digito_E01_2 = 8;
const int digito_E02_1 = 9;
const int digito_E02_2 = 10;
const int entrada_R = 11;

// Variables globales
char estado_actual = '0';
bool primer_loop = true;
struct Estado {
  bool estacion1[2];
  bool estacion2[2];
  bool brazoRobot;
};
Estado estadoActual;

// Prototipos de funciones
void inicializarPines();
void leerEntradas();
void procesarEstado();
void actualizarSalidas();
char f_transicion(char estado, Estado estadoActual);

void setup() {
  inicializarPines();
  Serial.begin(9600);
  Serial.println("Sistema iniciado. Esperando entradas...");
}

void loop() {
  leerEntradas();
  procesarEstado();
  actualizarSalidas();
}

void inicializarPines() {
  pinMode(salida_E01, OUTPUT);
  pinMode(salida_E02, OUTPUT);
  pinMode(digito_R_1, OUTPUT);
  pinMode(digito_R_2, OUTPUT);
  pinMode(digito_R_3, OUTPUT);
  pinMode(digito_E01_1, INPUT);
  pinMode(digito_E01_2, INPUT);
  pinMode(digito_E02_1, INPUT);
  pinMode(digito_E02_2, INPUT);
  pinMode(entrada_R, INPUT);
}

void leerEntradas() {
  estadoActual.estacion1[0] = digitalRead(digito_E01_1);
  estadoActual.estacion1[1] = digitalRead(digito_E01_2);
  estadoActual.estacion2[0] = digitalRead(digito_E02_1);
  estadoActual.estacion2[1] = digitalRead(digito_E02_2);
  estadoActual.brazoRobot = digitalRead(entrada_R);
}

void procesarEstado() {
  estado_actual = f_transicion(estado_actual, estadoActual);
}

void actualizarSalidas() {
  // Actualiza las salidas en función del estado actual
  switch (estado_actual) {
    case '0':
      digitalWrite(salida_E01, LOW);
      digitalWrite(salida_E02, LOW);
      break;
    case '1':
      digitalWrite(salida_E01, HIGH);
      digitalWrite(salida_E02, LOW);
      break;
    case '2':
      digitalWrite(salida_E01, LOW);
      digitalWrite(salida_E02, HIGH);
      break;
    case '3':
      digitalWrite(salida_E01, HIGH);
      digitalWrite(salida_E02, HIGH);
      break;
    default:
      Serial.println("Estado desconocido");
      break;
  }
}

char f_transicion(char estado, Estado estadoActual) {
  switch (estado) {
    case '0':
      if (estadoActual.estacion1[0] == LOW && estadoActual.estacion1[1] == LOW) {
        return '1';
      } else if (estadoActual.estacion2[0] == LOW && estadoActual.estacion2[1] == LOW) {
        return '2';
      } else if (estadoActual.estacion2[0] == HIGH && estadoActual.estacion2[1] == LOW) {
        return '3';
      }
      break;
    case '1':
      if (estadoActual.brazoRobot == HIGH) {
        return '0';
      }
      break;
    case '2':
      if (estadoActual.brazoRobot == HIGH) {
        return '0';
      }
      break;
    case '3':
      if (estadoActual.estacion1[0] == HIGH && estadoActual.estacion1[1] == HIGH) {
        return '4';
      }
      break;
    case '4':
      Serial.println("Estado final alcanzado");
      break;
    default:
      Serial.println("Transición desconocida");
      break;
  }
  return estado;
}