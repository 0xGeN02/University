#include <Arduino.h>

// Pin definitions
enum Pins {
  SALIDA_E01 = 2,
  SALIDA_E02 = 3,
  ROBOT_1 = 4,
  ROBOT_2 = 5,
  ROBOT_3 = 6,
  E01_1 = 7,
  E01_2 = 8,
  E02_1 = 9,
  E02_2 = 10,
  ROBOT = 11
};

// Station states
const uint8_t STATION_EMPTY = 0b00;
const uint8_t STATION_BUSY = 0b01;
const uint8_t STATION_DONE = 0b10;

// Robot commands
enum RobotCommand {
  ROBOT_IDLE = 0,
  ROBOT_TO_STATION1 = 1,
  ROBOT_TO_STATION2 = 2,
  ROBOT_TRANSFER = 3
};

class Estado {
private:
  uint8_t station1_state : 2;
  uint8_t station2_state : 2;
  uint8_t robot_state : 1;

public:
  Estado() : station1_state(0), station2_state(0), robot_state(0) {}
  
  void setStation1(uint8_t state) { station1_state = state & 0b11; }
  void setStation2(uint8_t state) { station2_state = state & 0b11; }
  void setRobot(bool state) { robot_state = state; }
  
  uint8_t getStation1() const { return station1_state; }
  uint8_t getStation2() const { return station2_state; }
  bool getRobot() const { return robot_state; }
  
  bool hasChanged(const Estado& other) const {
    return station1_state != other.station1_state ||
           station2_state != other.station2_state ||
           robot_state != other.robot_state;
  }
};

class StateMachine {
private:
  char current_state;
  char previous_state;
  Estado current_estado;
  Estado previous_estado;

  void readInputs() {
    uint8_t s1_state = (digitalRead(Pins::E01_2) << 1) | digitalRead(Pins::E01_1);
    uint8_t s2_state = (digitalRead(Pins::E02_2) << 1) | digitalRead(Pins::E02_1);
    
    previous_estado = current_estado;
    current_estado.setStation1(s1_state);
    current_estado.setStation2(s2_state);
    current_estado.setRobot(digitalRead(Pins::ROBOT));
  }

  void sendRobotCommand(RobotCommand cmd) {
    digitalWrite(Pins::ROBOT_1, cmd & 0b001);
    digitalWrite(Pins::ROBOT_2, cmd & 0b010);
    digitalWrite(Pins::ROBOT_3, cmd & 0b100);
  }

  void updateOutputs() {
    switch (current_state) {
      case '0':
        digitalWrite(Pins::SALIDA_E01, LOW);
        digitalWrite(Pins::SALIDA_E02, LOW);
        break;
      case '1':
        digitalWrite(Pins::SALIDA_E01, HIGH);
        digitalWrite(Pins::SALIDA_E02, LOW);
        break;
      case '2':
        digitalWrite(Pins::SALIDA_E01, LOW);
        digitalWrite(Pins::SALIDA_E02, HIGH);
        break;
      case '3':
        digitalWrite(Pins::SALIDA_E01, HIGH);
        digitalWrite(Pins::SALIDA_E02, HIGH);
        break;
    }

    if (current_estado.hasChanged(previous_estado)) {
      handleStateChange();
    }
  }

  void handleStateChange() {
    switch (current_state) {
      case '1':
        if (previous_state == '0') {
          sendRobotCommand(ROBOT_TO_STATION1);
        }
        break;
      case '2':
        if (previous_state == '0') {
          sendRobotCommand(ROBOT_TO_STATION2);
        }
        break;
      case '3':
        if (previous_state == '2') {
          sendRobotCommand(ROBOT_TRANSFER);
        }
        break;
      default:
        sendRobotCommand(ROBOT_IDLE);
        break;
    }
  }

  char calculateNextState() {
    switch (current_state) {
      case '0':
        if (current_estado.getStation1() == STATION_EMPTY) return '1';
        if (current_estado.getStation2() == STATION_EMPTY) return '2';
        if (current_estado.getStation2() == STATION_BUSY) return '3';
        break;
      case '1':
      case '2':
        if (current_estado.getRobot()) return '0';
        break;
      case '3':
        if (current_estado.getStation1() == STATION_DONE) return '4';
        break;
    }
    return current_state;
  }

public:
  StateMachine() : current_state('0'), previous_state('0') {}

  void init() {
    pinMode(Pins::SALIDA_E01, OUTPUT);
    pinMode(Pins::SALIDA_E02, OUTPUT);
    pinMode(Pins::ROBOT_1, OUTPUT);
    pinMode(Pins::ROBOT_2, OUTPUT);
    pinMode(Pins::ROBOT_3, OUTPUT);
    pinMode(Pins::E01_1, INPUT);
    pinMode(Pins::E01_2, INPUT);
    pinMode(Pins::E02_1, INPUT);
    pinMode(Pins::E02_2, INPUT);
    pinMode(Pins::ROBOT, INPUT);
  }

  void update() {
    previous_state = current_state;
    readInputs();
    current_state = calculateNextState();
    updateOutputs();
  }
};

StateMachine stateMachine;

void setup() {
  stateMachine.init();
  Serial.begin(9600);
  Serial.println("Sistema iniciado. Esperando entradas...");
}

void loop() {
  stateMachine.update();
}