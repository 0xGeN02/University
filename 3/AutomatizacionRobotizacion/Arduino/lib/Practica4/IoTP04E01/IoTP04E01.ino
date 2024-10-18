// Asignatura: TAyRE
// Prácticas de IoT
// Programa: IoTP04E01.ino   
// Placa Arduino Uno
// Sensor de Temperatura TPM36
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 18/08/2024        
// BIBLIOTECAS
   #include <LiquidCrystal.h>

// DEFINICIÓN DE VARIABLES Y CONSTANTES GLOBALES 
   const int PIN_TPM36 = A0; // Pin al que está conectado el TMP36

   LiquidCrystal LCD1(12, 11, 5, 4, 3, 2);  

// DEFINICIÓN DE PROTOTIPOS DE RUTINAS
   float Voltaje  ( int ); // Convierte Entrada a Voltaje
   float T_Celsius(float); // Cálcula la Temperatura en Grados Celsius

// BLOQUE DE INICIALIZACIÓN 

   void setup()
   {
    LCD1.begin(16, 2); // LCD
    LCD1.clear();
    LCD1.setCursor(0,0);
    LCD1.print("SENSOR TPM36");
    LCD1.setCursor(0,1);
    LCD1.print("Temp. = ");
   }

// BLOQUE DE EJECUCIÓN

void loop()
{
  float T;
  T=T_Celsius(Voltaje(analogRead(PIN_TPM36)));
  LCD1.setCursor(8,1);
  LCD1.print(T);
  delay(1000); // Espera un segundo antes de hacer la próxima lectura
}
// FIN BLOQUE EJECUCIÓN

// DECLARACIONES DE RUTINAS
// RUTINA  Voltaje Tipo: Función float
// Parámetros:
//    1. TPM36 Tipo Entero
// Convertir la lectura del sensor TPM36 en voltios
// RETORNA: Un número real (float) con el valor de voltaje.
float Voltaje(int TMP36)
{
   return (TMP36*5000.0/1024.0);
}

// RUTINA T_Celsius  Tipo Función float
// Parámetros:
// V Tipo Real  Voltaje.
// Convertir voltios a temperatura.
// RETORNA: Un número real (float) con el valor de voltaje.
float T_Celsius(float V)
{
 return ((V-500.0)/10.0);
}
