#include <Arduino.h>
#include <LiquidCrystal.h>

// Pines del LCD
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Pines y variables del sensor SHARP GP2Y0A21
const int sensorPin = A0;
int sensorValue = 0;
float distance = 0.0;

// Pines y variables del LED
const int ledPin = 13;
int ledState = LOW;

// Umbrales y estado
int Umbral[] = {170, 340, 510, 680, 850};
int Estado = 0;
int EA = 0;

// Prototipos de funciones
void Inicializar_Pines(int, int);
int F_Transision_Estados(int, int, int[]);
void Encender(int);
void Salida_Serial(int, int);

void setup() {
    Inicializar_Pines(ledPin, 1);
    Serial.begin(9600); // Inicialización puerto Serial
    lcd.begin(16, 2); // Inicialización del LCD
    Salida_Serial(Estado, 0); // Muestra Inicial
    Encender(0);
}

void loop() {
    int Evento; // Variable que recibe el valor de la función analogRead()
    sensorValue = analogRead(sensorPin);
    distance = (6787.0 / (sensorValue - 3.0)) - 4.0; // Conversión del valor analógico a distancia en cm
    Evento = sensorValue;
    Estado = F_Transision_Estados(Estado, Evento, Umbral);
    if (EA != Evento) {
        Encender(Estado);
        Salida_Serial(Estado, Evento);
        Mostrar_LCD(distance, Estado);
    }
    EA = Evento;
}

void Inicializar_Pines(int pinI, int totalPines) {
    pinMode(pinI, OUTPUT);
}

int F_Transision_Estados(int estado, int evento, int umbrales[]) {
    if (evento < umbrales[0]) {
        return 0;
    } else if (evento < umbrales[1]) {
        return 1;
    } else if (evento < umbrales[2]) {
        return 2;
    } else if (evento < umbrales[3]) {
        return 3;
    } else if (evento < umbrales[4]) {
        return 4;
    } else {
        return 5;
    }
}

void Encender(int estado) {
    if (estado == 0) {
        digitalWrite(ledPin, LOW);
        ledState = LOW;
    } else {
        digitalWrite(ledPin, HIGH);
        ledState = HIGH;
    }
}

void Salida_Serial(int estado, int evento) {
    Serial.println("-----------------------------------");
    Serial.print("    ESTADO : "); Serial.print(estado);
    Serial.print("    ENTRADA : "); Serial.println(evento);
    Serial.println("-----------------------------------");
}

void Mostrar_LCD(float distancia, int estado) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Distancia: ");
    lcd.print(distancia);
    lcd.print(" cm");
    lcd.setCursor(0, 1);
    lcd.print("LED: ");
    if (estado == 0) {
        lcd.print("Apagado");
    } else {
        lcd.print("Encendido");
    }
}