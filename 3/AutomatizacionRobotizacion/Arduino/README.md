
# Instalación de Arduino CLI, Configuración de VSCode y PlatformIO

Este documento detalla cómo instalar y configurar **Arduino CLI**, **Visual Studio Code (VSCode)** y **PlatformIO** para trabajar con Arduino en Windows y Linux. También incluye instrucciones para compartir y reutilizar esta configuración en otro ordenador.

---

## Paso 1: Instalar Arduino CLI

### Descargar e Instalar Arduino CLI
- **Windows:**
  1. Ve a la [página oficial de Arduino CLI](https://github.com/arduino/arduino-cli/releases).
  2. Descarga el archivo `.zip` correspondiente a Windows y extrae su contenido.
  3. Añade la ruta de `arduino-cli.exe` a la variable de entorno `PATH`.

- **Linux:**
  1. Abre una terminal y ejecuta:
     ```bash
     curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
     ```
  2. Agrega `arduino-cli` al `PATH` de tu sistema añadiendo la línea correcta en tu `.bashrc` o `.zshrc`:
     ```bash
     export PATH="$PATH:/ruta/a/arduino-cli"
     ```

---

## Paso 2: Configurar Arduino CLI

### Actualizar el Índice de Cores
Abre una terminal y ejecuta:
```bash
arduino-cli core update-index
```

### Instalar el Core de Arduino AVR
Para trabajar con una placa como el Arduino Uno, instala el core AVR ejecutando:
```bash
arduino-cli core install arduino:avr
```

### Verificar la Instalación
Verifica que el core se haya instalado correctamente con el siguiente comando:
```bash
arduino-cli core list
```

---

## Paso 3: Configurar Visual Studio Code (VSCode)

### Instalar la Extensión de C/C++
1. Abre **Visual Studio Code**.
2. Ve a la pestaña de **Extensiones** (`Ctrl+Shift+X`).
3. Busca e instala la extensión **C/C++** de Microsoft.

### Instalar PlatformIO
1. En la pestaña de **Extensiones** (`Ctrl+Shift+X`), busca **PlatformIO IDE** e instálalo.
2. Reinicia VSCode para activar la extensión.

### Crear el Entorno `platformio_env`
1. Abre **PlatformIO** y crea un nuevo proyecto (`PlatformIO: New Project`).
2. Selecciona tu placa Arduino (ej. Arduino Uno) y crea un entorno llamado `platformio_env`.

---

## Paso 4: Configurar PlatformIO y c_cpp_properties.json

### Configurar el Archivo `c_cpp_properties.json`
1. Abre la paleta de comandos (`Ctrl+Shift+P`) y selecciona:
   - **C/C++: Edit Configurations (UI)**.
2. Abre el archivo JSON y actualiza las rutas con la ubicación de las herramientas y librerías de Arduino CLI.

   Aquí tienes un ejemplo para Windows:
   ```json
   {
     "configurations": [
       {
         "name": "Win32",
         "includePath": [
           "${workspaceFolder}/**",
           "C:/Program Files (x86)/arduino-cli/libraries",
           "C:/Program Files (x86)/arduino-cli/tools"
         ],
         "compilerPath": "C:/Program Files (x86)/arduino-cli/bin/gcc",
         "cStandard": "c11",
         "cppStandard": "c++17"
       }
     ],
     "version": 4
   }
   ```

   Y para Linux:
   ```json
   {
     "configurations": [
       {
         "name": "Linux",
         "includePath": [
           "${workspaceFolder}/**",
           "/usr/local/bin/arduino-cli/libraries",
           "/usr/local/bin/arduino-cli/tools"
         ],
         "compilerPath": "/usr/bin/gcc",
         "cStandard": "c11",
         "cppStandard": "c++17"
       }
     ],
     "version": 4
   }
   ```

---

## Paso 5: Guardar y Compartir la Configuración

Guarda el archivo `c_cpp_properties.json` en el directorio `.vscode` de tu proyecto. Si deseas usar esta configuración en otro PC, copia el directorio `.vscode` junto con tu proyecto.

---

## Paso 6: Compilar y Subir el Código

### Compilar el Proyecto
1. Abre la paleta de comandos (`Ctrl+Shift+P`).
2. Escribe "PlatformIO: Build" para compilar el proyecto.

### Subir el Código a la Placa
1. Escribe "PlatformIO: Upload" para subir el código a la placa.

---

## Paso 7: Monitorear el Puerto Serie

### Abrir el Monitor Serie
1. Abre la paleta de comandos (`Ctrl+Shift+P`).
2. Escribe "PlatformIO: Serial Monitor" para abrir el monitor serie.

---

## Resumen

1. **Instalar Arduino CLI** en Windows o Linux.
2. **Configurar Visual Studio Code** instalando la extensión de C/C++ y PlatformIO.
3. **Crear y configurar el archivo `c_cpp_properties.json`** con las rutas correctas.
4. **Guardar y compartir la configuración** copiando el directorio `.vscode` junto con tu proyecto.
5. **Compilar y subir el código** usando PlatformIO en VSCode.
6. **Monitorear el puerto serie** con el monitor serie de PlatformIO.
