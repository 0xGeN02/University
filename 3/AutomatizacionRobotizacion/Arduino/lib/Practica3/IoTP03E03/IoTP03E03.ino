// Asignatura: TAyRE
// Programa: IoTP03E03.ino   
// Placa Arduino Uno
// Pantalla Cristal Líquido LCD 16x2
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 14/08/2024        
// Inclusión de Bibliotecas
   #include <LiquidCrystal.h>
// Prototipos de Funciones
   void Iniciar();
   void Numeros();
// BLOQUE DE INICIALIZACIÓN
LiquidCrystal LCD1(12, 11, 5, 4, 3, 2);
void setup() 
{
 LCD1.begin(16, 2);
}
// INICIO BLOQUE EJECUCIÓN
void loop() 
{
 Iniciar();
 LCD1.setCursor(3, 0);
 LCD1.print("IoTP03E03");
 LCD1.setCursor(1, 1);  
 Numeros();
 Finalizar();
}
// FIN BLOQUE EJECUCIÓN
// DECLARACIONES DE FUNCIONES
// FUNCIÓN DE INICIO
void Iniciar()
{
  LCD1.clear();
  LCD1.setCursor(6, 0);
  LCD1.print("UIE");
  LCD1.setCursor(0, 1);
  LCD1.print("Laboratorio IoT");
  delay(3000);
  LCD1.clear();
}
//FUNCIÓN MOSTRAR NÚMEROS [0,7]
void Numeros()
{
  int c;
  for(c = 0; c < 8; c++) 
  {                                   
    LCD1.print(c);   
    LCD1.print(" ");    
    delay(500);                       
  }  
}
// FUNCIÓN PARA FINALIZAR LA PRUEBA
void Finalizar()
{
  for(int i = 4; i > 0; i -= 1) 
  {
    LCD1.clear();
    LCD1.setCursor(6, 0);
    LCD1.print("UIE");
    delay(300);
    LCD1.clear();
    delay(300);
  }  
}