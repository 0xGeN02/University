// Asignatura: TAyRE
// Programa: P01E01.ino   
// Iniciación con Placa Arduino Uno
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 05/08/2024        
// BIBLIOTECAS
#include "IoT_P01_E01.h"
// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES

// DECLARACION DE RUTINAS
// Rutina PARPADEO DE UN LED
void PARPADEO(int Pin, int Seg){
  int delayTime = Seg*1000; //miliseconds to seconds

  digitalWrite(Pin, HIGH);   
  delay(delayTime);              
  
  digitalWrite(Pin, LOW);    
  delay(delayTime);    
}