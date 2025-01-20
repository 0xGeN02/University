// Constantes
// ESTACIÓN 2
  const int verde = 2;
  const int ambar = 3;
  const int rojo = 4;
  char estado_inicial = ' ';
  char estadoActual = ' ';
  unsigned long tiempo_inicio; // Tiempo de inicio para el proceso de Estación 2
  const int digito_1 = 5;
  const int digito_2 = 6;
  
// Entrada digital
const int input_supervisor = 8; // Define el pin de entrada digital

// Variables globales
bool digIn;                 // Estado del pin de entrada digital

// DECLARACIÓN PROTOTIPOS DE RUTINAS
char f_transicion(char estadoActual, bool digIn);
void out_putAssign(char estadoActual);

void setup() {
  // Estación 2
  pinMode(verde, OUTPUT);
  pinMode(ambar, OUTPUT);
  pinMode(rojo, OUTPUT);
  pinMode(digito_1, OUTPUT);
  pinMode(digito_2, OUTPUT);
  estado_inicial = '0';  // Estado inicial para Estación 2
  estadoActual = estado_inicial;

  // Configurar pin de entrada digital
  pinMode(input_supervisor, INPUT);

  Serial.begin(9600);
  Serial.println("Sistema iniciado - Esperando digIns");
}

void loop() {
  // Leer entrada digital
  digIn = digitalRead(input_supervisor);
  // Estado actual
  estadoActual = f_transicion( estadoActual,  digIn);
  // Actualizar salida según los estados
  outputAssign(estadoActual);
}

// DEFINICIÓN DE FUNCIONES

// Funcion de transicion para la estacion 2

char f_transicion(char estadoActual, bool digIn ) {
  static bool temporizador_iniciado = false;
  // Estado 0 al Estado 1

  if (estadoActual == '0' && digIn == 1 ) {
    Serial.println("Estacion 2: Disponible");
    temporizador_iniciado = true;
    tiempo_inicio = millis(); // Comienza el tiempo inicio 3
    return '1'; // Se pasa al estado 1
  }

  // Estado 1 a Estado 2 

  if (estadoActual == '1' && temporizador_iniciado) {
    if (millis() - tiempo_inicio >= 2000) { // 2 segundos han pasado
      Serial.println("Estacion 2: Acabado mecanizado 1 ");
      temporizador_iniciado = false;
     
      return '2';  // Se pasa al estado 2
    }
  }
  
  // Pasar del Estado 2 a 0

  if (estadoActual == '2' && digIn == 0){
    Serial.println("Estacion 2: Disponible");
    return '0';
  }
  return estadoActual;
}

void outputAssign(char estadoActual) {
  // Luz verde
  if (estadoActual == '0') {
    digitalWrite(rojo, LOW);
    digitalWrite(ambar, LOW);
    digitalWrite(verde, HIGH);
    digitalWrite(digito_1, LOW);
    digitalWrite(digito_2, LOW);
  }
  // Luz roja
  else if (estadoActual == '1') {
    digitalWrite(rojo, HIGH);
    digitalWrite(ambar, LOW);
    digitalWrite(verde, LOW);
    digitalWrite(digito_1, LOW);
    digitalWrite(digito_2, HIGH);
  }
  // Luz amarilla
  else if (estadoActual == '2') {
    digitalWrite(rojo, LOW);
    digitalWrite(ambar, HIGH);
    digitalWrite(verde, LOW);
    digitalWrite(digito_1, HIGH);
    digitalWrite(digito_2, LOW);
  }
}