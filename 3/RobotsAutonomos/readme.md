# RobotsAutonomos

Este proyecto utiliza el SDK de iRobot para controlar robots autónomos. A continuación se detallan los pasos para configurar el entorno virtual y las dependencias necesarias.

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Configuración del Entorno Virtual

### 1. Crear y Activar el Entorno Virtual

#### En Windows:
```sh
python -m venv irobot_env
.\irobot_env\Scripts\activate
```

#### En Linux:
```sh
python3 -m venv irobot_env
source irobot_env/bin/activate
```

### 2. Instalar dependencias

Una vez que el entorno virtual esté activado, instala las dependencias necesarias desde el archivo `requirements.txt`:

```sh
pip install -r requirements.txt
```
### 3. Instalar irobot sdk

```sh
git submodule init
git submodule update
```

```sh
cd irobot-edu-python-sdk
pip3 install .
```
## Uso del proyecto

### 1. Activar venv

#### Windows
```sh
.\irobot_env\Scripts\activate
```

#### Linux
```sh
source irobot_env/bin/activate
```

