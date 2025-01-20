// Constantes

// Salidas digitales
const int salida_E01 = 6; // Estación 1     0: Sin Pieza     1: Con pieza
const int salida_E02 = 7; // Estación 2     0: Sin Pieza     1: Con pieza
const int digito_R_1 = 8; // Brazo Robot D1
const int digito_R_2 = 9; // D2
const int digito_R_3 = 10; // D3
// 000: Disponible 001: P1  010: P2 011: P3 100: P4

// Entradas digitales
const int digito_E01_1 = 2; // Estación 1 00: Disponible     01: Trabajo A     10: Trabajo B      11: Trabajo Finalizado
const int digito_E01_2 = 3;
const int digito_E02_1 = 4; // Estación 2 00: Disponible     01: Trabajo.      10: Trabajo Finalizado
const int digito_E02_2 = 5;
const int entrada_R = 11;   // Brazo Robot 0: Disponible.    1: Ocupado

// Variables globales
char estadoActual = '0'; // Estado inicial
bool estado_digito_E01_1, estado_digito_E01_2;
bool estado_digito_E02_1, estado_digito_E02_2;
bool estado_entrada_R;
bool P2_en_AE = false; // Inicialización de P2_en_AE

// Prototipos
char f_transicion(char estadoActual, bool estado_digito_E01_1, bool estado_digito_E01_2,
                  bool estado_digito_E02_1, bool estado_digito_E02_2, bool estado_entrada_R,
                  bool &P2_en_AE);  // P2_en_AE como referencia
void outputAssign(char estadoActual);

void setup() {
  // Configurar pines de salida
  pinMode(salida_E01, OUTPUT);
  pinMode(salida_E02, OUTPUT);
  pinMode(digito_R_1, OUTPUT);
  pinMode(digito_R_2, OUTPUT);
  pinMode(digito_R_3, OUTPUT);

  // Configurar pines de entrada
  pinMode(digito_E01_1, INPUT);
  pinMode(digito_E01_2, INPUT);
  pinMode(digito_E02_1, INPUT);
  pinMode(digito_E02_2, INPUT);
  pinMode(entrada_R, INPUT);

  Serial.begin(9600);
  Serial.println("Sistema iniciado. Esperando entradas...");
}

void loop() {
  // Leer estados de las entradas digitales
  estado_digito_E01_1 = digitalRead(digito_E01_1);
  estado_digito_E01_2 = digitalRead(digito_E01_2);
  estado_digito_E02_1 = digitalRead(digito_E02_1);
  estado_digito_E02_2 = digitalRead(digito_E02_2);
  estado_entrada_R = digitalRead(entrada_R);

  // Actualizar el estado actual y P2_en_AE
  estadoActual = f_transicion(estadoActual, estado_digito_E01_1, estado_digito_E01_2,
                              estado_digito_E02_1, estado_digito_E02_2, estado_entrada_R, P2_en_AE);

  // Actualizar salidas según el estado
  outputAssign(estadoActual);
}

// Función de transición
char f_transicion(char estadoActual, bool digito_E01_1, bool digito_E01_2,
                  bool digito_E02_1, bool digito_E02_2, bool entrada_R, bool &P2_en_AE) {

  // Proceso 1: Llevar Pieza Base 1 a Estación 1
  if (entrada_R == 0 && digito_E01_1 == 0 && digito_E01_2 == 0) {
    Serial.println("Llevar Pieza Base 1 a Estación 1");
    return '1';  // Cambiar al estado 1
  }

  // Proceso 2: Llevar Pieza Base 2 a Estación 2
  if (entrada_R == 0 && digito_E02_1 == 0 && digito_E02_2 == 0) {
    Serial.println("Llevar Pieza Base 2 a Estación 2");
    return '2';  // Cambiar al estado 2
  }

  // Proceso 3: Llevar Pieza P2 de Estación 2 al Área de Ensamblado
  if (entrada_R == 0 && digito_E02_1 == 1 && digito_E02_2 == 0) {
    Serial.println("Llevar Pieza P2 de Estación 2 al Área de Ensamblado");
    P2_en_AE = true;  // P2 ha sido colocado en el área de ensamblado
    return '3';  // Cambiar al estado 3
  }

  // Proceso 4: Llevar Pieza P1 de Estación 1 al Área de Ensamblado y ensamblar con P2
  if (entrada_R == 0 && digito_E01_1 == 1 && digito_E01_2 == 1 && P2_en_AE == true) {
    Serial.println("Llevar Pieza P1 de Estación 1 al Área de Ensamblado y ensamblar con P2");
    P2_en_AE = false;  // Después de ensamblar, P2 ya no está en el área de ensamblado
    return '4';  // Cambiar al estado 4
  }

  return estadoActual; // Mantener el estado si no hay transición
}

void outputAssign(char estadoActual) {
  // Disponible
  if (estadoActual == '0') {
    digitalWrite(digito_R_1, LOW);
    digitalWrite(digito_R_2, LOW);
    digitalWrite(digito_R_3, LOW);
  }
  // Proceso 1
  else if (estadoActual == '1') {
    digitalWrite(digito_R_1, LOW);
    digitalWrite(digito_R_2, LOW);
    digitalWrite(digito_R_3, HIGH);
    digitalWrite(salida_E01, HIGH); // Estación 1 ocupada
  }
  // Proceso 2
  else if (estadoActual == '2') {
    digitalWrite(digito_R_1, LOW);
    digitalWrite(digito_R_2, HIGH);
    digitalWrite(digito_R_3, LOW);
    digitalWrite(salida_E02, HIGH); // Estación 2 ocupada
  }
  // Proceso 3
  else if (estadoActual == '3') {
    digitalWrite(digito_R_1, LOW);
    digitalWrite(digito_R_2, HIGH);
    digitalWrite(digito_R_3, HIGH);
    digitalWrite(salida_E02, LOW);  // Estación 1 disponible
  }
  // Proceso 4
  else if (estadoActual == '4') {
    digitalWrite(digito_R_1, HIGH);
    digitalWrite(digito_R_2, LOW);
    digitalWrite(digito_R_3, LOW);
    digitalWrite(salida_E01, LOW);  // Estación 2 disponible
  }
}