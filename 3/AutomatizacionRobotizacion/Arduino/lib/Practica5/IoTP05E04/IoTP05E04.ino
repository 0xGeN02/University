// Asignatura: TAyRE
// Programa: IoTP05E04_SensorInductivo.ino
// Placa Arduino Uno
// Sensor Inductivo WPSE476
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha: 14/08/2024        

// PROTOTIPOS DE RUTINAS
void Verificar_Objeto();

// DECLARACIONES Y DEFINICIONES
// CONSTANTES
const int Pin_Sensor = 8;    // Pin digital para el sensor inductivo
const int Pausa = 500;       // Pausa entre verificaciones

// BLOQUE DE INICIALIZACIÓN 
void setup() {
  // Configuración del pin asociado al sensor inductivo
  pinMode(Pin_Sensor, INPUT);

  // Inicialización del puerto serial
  Serial.begin(9600);
  Serial.println("Iniciando prueba del sensor inductivo WPSE476");
}

void loop() {
  Verificar_Objeto();
  delay(Pausa); // Pausa de medio segundo entre lecturas
}

// DECLARACIONES DE RUTINAS

// Verificar_Objeto
// Lee el estado del sensor inductivo y envía la información al monitor serial
void Verificar_Objeto() {
  int estado_sensor = digitalRead(Pin_Sensor); // Lee el estado del sensor (HIGH o LOW)

  if (estado_sensor == HIGH) {
    Serial.println("No hay objeto");
  } else {
    Serial.println("Objeto Detectado");
  }
}

