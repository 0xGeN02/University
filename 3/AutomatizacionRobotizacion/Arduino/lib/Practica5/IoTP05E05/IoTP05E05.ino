// Asignatura: TAyRE
// Programa: IoTP05E05.ino
// Encender y Apagar un Motor DC y Sentido de Giro
// Placa Arduino Uno, Integrado L293D, Motor DC, 3 LEDS, Sensor Inductivo WPSE476
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        

// PROTOTIPOS DE RUTINAS
void MotorControl(int, int, int, int);
void Motor_OFF(int, int, int);
void Verificar_Objeto();
void ActualizarEstados();

// CONSTANTES
// PINES ASOCIADOS AL INTEGRADO L293D
const int Activar = 11;
const int Entrada_1 = 10;
const int Entrada_2 = 9;

// PINES ASOCIADOS A LEDS
const int Pin_V = 8;     // Pin Verde Disponible
const int Pin_A = 7;     // Pin Amarillo Esperando
const int Pin_R = 6;     // Pin Rojo Ocupado

// Sensor Inductivo WPSE476
const int Pin_Sensor = 12;    // Pin digital para el sensor inductivo
const unsigned long T = 3000; // Tiempo en milisegundos para el motor en estado Ocupado

// Variables de estado
int Estado_Actual = 0; // 0: Disponible, 1: Ocupado, 2: Esperando
unsigned long inicioTiempoMotor = 0;
bool motorEncendido = false;
bool objetoDetectado = false;

// BLOQUE DE INICIALIZACIÓN 
void setup() {
    // Pines de Salida L293D 
    pinMode(Activar, OUTPUT);
    pinMode(Entrada_1, OUTPUT);
    pinMode(Entrada_2, OUTPUT);

    // Configuración del pin asociado al sensor inductivo
    pinMode(Pin_Sensor, INPUT);

    // Configuración de pines para LEDs
    pinMode(Pin_V, OUTPUT);   // Verde
    pinMode(Pin_A, OUTPUT);   // Amarillo
    pinMode(Pin_R, OUTPUT);   // Rojo

    // Puerto Serial 
    Serial.begin(9600);
    Serial.println("Iniciando prueba del E05");

    // Estado Inicial Motor Disponible
    Estado_Actual = 0;
    ActualizarEstados();
}

// BLOQUE DE EJECUCIÓN
void loop() {
    Verificar_Objeto();  // Monitoreo del estado del sensor

    // Lógica de temporización para el motor en estado "Ocupado"
    if (Estado_Actual == 1 && motorEncendido) {
        if (millis() - inicioTiempoMotor >= T) {
            motorEncendido = false;
            Estado_Actual = 2; // Cambiar a estado "Esperando"
            ActualizarEstados();
            Serial.println("Motor: Apagado (Esperando)");
        }
    }
}

// FUNCIONES AUXILIARES

// Actualiza las luces de los LEDs según el estado actual
void ActualizarEstados() {
    // Apagar todos los LEDs
    digitalWrite(Pin_V, LOW);
    digitalWrite(Pin_A, LOW);
    digitalWrite(Pin_R, LOW);

    // Encender LEDs según el estado actual
    switch (Estado_Actual) {
        case 0: // Verde - Disponible
            digitalWrite(Pin_V, HIGH);
            Motor_OFF(Activar, Entrada_1, Entrada_2); // Motor apagado
            Serial.println("Motor: Disponible");
            break;

        case 1: // Rojo - Ocupado  
            digitalWrite(Pin_R, HIGH);
            MotorControl(Activar, Entrada_1, Entrada_2, 0); // Motor encendido hacia la izquierda
            inicioTiempoMotor = millis();
            motorEncendido = true;
            Serial.println("Motor: Ocupado (girando)");
            break;

        case 2: // Amarillo - Esperando
            digitalWrite(Pin_A, HIGH);
            Motor_OFF(Activar, Entrada_1, Entrada_2); // Motor apagado
            Serial.println("Motor: Esperando");
            break;
    }
}

// Monitorea el estado del sensor inductivo
void Verificar_Objeto() {
    bool estado_sensor = digitalRead(Pin_Sensor) == LOW;

    if (estado_sensor && Estado_Actual == 0) { // Si está en "Disponible" y detecta un objeto
        Estado_Actual = 1; // Cambiar a "Ocupado"
        objetoDetectado = true;
        ActualizarEstados();
        Serial.println("Objeto Detectado");
    } else if (!estado_sensor && objetoDetectado) {
        objetoDetectado = false;
        Serial.println("Objeto Removido");
    }
    if (!estado_sensor && Estado_Actual == 2) {  // Si no detecta objeto y está en "Esperando"
      Estado_Actual = 0; // Cambiar a "Ocupado"
      ActualizarEstados();
    }
}

// Controla el motor para que gire a la izquierda o derecha
void MotorControl(int E, int E1, int E2, int D) {
    analogWrite(E, 255); // Velocidad máxima
    if (D == 0) {
        digitalWrite(E1, HIGH);
        digitalWrite(E2, LOW);
    } else {
        digitalWrite(E1, LOW);
        digitalWrite(E2, HIGH);
    }
}

// Apaga el motor DC
void Motor_OFF(int E, int E1, int E2) {
    digitalWrite(E, LOW);
    digitalWrite(E1, LOW);
    digitalWrite(E2, LOW);
}
