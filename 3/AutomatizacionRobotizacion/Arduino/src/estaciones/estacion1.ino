// Constantes
// ESTACIÓN 1
  const int verde = 2;
  const int ambar = 3;
  const int rojo = 4;
  char estado_inicial = ' ';
  char estadoActual = ' ';
  unsigned long tiempo_inicio_1; // Tiempo de inicio para el proceso de Estación 1
  unsigned long tiempo_inicio_2;
  const int digito_1 = 5;
  const int digito_2 = 6;
  
// Entrada digital
const int input_supervisor = 8; // Define el pin de entrada digital

// Variables globales
bool digIn;                 // Estado del pin de entrada digital

// DECLARACIÓN PROTOTIPOS DE RUTINAS
char f_transicion(char estadoActual, bool digIn);
void outputAssign(char estadoActual);

void setup() {
  // Estación 1
  pinMode(verde, OUTPUT);
  pinMode(ambar, OUTPUT);
  pinMode(rojo, OUTPUT);
  pinMode(digito_1, OUTPUT);
  pinMode(digito_2, OUTPUT);
  estado_inicial = '0';  // Estado inicial para Estación 1
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
  // Actualizar salidas según los estados
  outputAssign(estadoActual);
}

// DEFINICIÓN DE FUNCIONES

// Funcion de transicion para la estacion 1 


// Provisionalmente digIn es igual a la entrada del teclado
char f_transicion(char estadoActual, bool digIn ) {
  static bool temporizador_iniciado_1 = false;
  static bool temporizador_iniciado_2 = false;


  // Estado 0 al Estado 1: Rojo

  if (estadoActual == '0' && digIn == 1) {
    Serial.println("Estación 1: Disponible");
    temporizador_iniciado_1 = true;
    tiempo_inicio_1 = millis(); // Comienza el tiempo inicio 1
    return '1'; // Se pasa al estado 1
  }

  // Estado 1 a Estado 2 : Rojo

  if (estadoActual == '1' && temporizador_iniciado_1) {
    if (millis() - tiempo_inicio_1 >= 5000) { // 5 segundos han pasado
      //Serial.println("Estacion 1: Acabado mecanizado 1 ");
      temporizador_iniciado_1 = false;
      temporizador_iniciado_2 = true;
      tiempo_inicio_2 = millis();
      return '2';  // Se pasa al estado 2
    }
  }
  // Estado 2 a Estado 3 : Amarillo

  if (estadoActual == '2' && temporizador_iniciado_2) {
    if (millis() - tiempo_inicio_2 >= 3000) { // 5 segundos han pasado
      //Serial.println("Estacion 1: Acabado mecanizado 2 ");
      temporizador_iniciado_2 = false;
      return '3';  // Se pasa al estado 3
    }
  }
  // Pasar del Estado 3 a 0: Verde

  if (estadoActual == '3' && digIn == 0){
    Serial.println("Estacion 1: Disponible");
    return '0';
  }

  return estadoActual;
  
}

void outputAssign(char estadoActual) {
  // Luz verde : estado 0
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
  // Luz roja
  else if (estadoActual == '2') {
    digitalWrite(rojo, HIGH);
    digitalWrite(ambar, LOW);
    digitalWrite(verde, LOW);
    digitalWrite(digito_1, HIGH);
    digitalWrite(digito_2, LOW);
  }
  // Luz amarilla
  else if (estadoActual == '3') {
    digitalWrite(rojo, LOW);
    digitalWrite(ambar, HIGH);
    digitalWrite(verde, LOW);
    digitalWrite(digito_1, HIGH);
    digitalWrite(digito_2, HIGH);
  }
}