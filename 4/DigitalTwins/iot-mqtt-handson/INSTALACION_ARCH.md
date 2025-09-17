# Instalación en Arch Linux - IoT MQTT Hands-On

## 1. Instalar dependencias del sistema

### Actualizar el sistema

```bash
sudo pacman -Syu
```

### Instalar Mosquitto MQTT Broker

```bash
sudo pacman -S mosquitto
```

### Instalar Node.js y npm

```bash
sudo pacman -S nodejs npm
```

### Instalar Python y pip

```bash
sudo pacman -S python python-pip
```

## 2. Configurar e iniciar Mosquitto

### Habilitar e iniciar el servicio

```bash
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### Verificar que está corriendo

```bash
sudo systemctl status mosquitto
```

### Probar conexión local

```bash
mosquitto_pub -h localhost -t test/topic -m "Hello MQTT"
mosquitto_sub -h localhost -t test/topic
```

## 3. Instalar Node-RED

### Instalar Node-RED globalmente

```bash
sudo npm install -g --unsafe-perm node-red
```

### Iniciar Node-RED

```bash
node-red
```

Acceder a: [http://localhost:1880]

## 4. Instalar dependencias Python

### Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate
```

### Instalar paho-mqtt

```bash
pip install paho-mqtt
```

## 5. Configuración adicional de Node-RED

Una vez que Node-RED esté corriendo:

1. Acceder a [http://localhost:1880]
2. Ir a Menú → Manage palette → Install
3. Buscar e instalar: `node-red-dashboard`
4. Reiniciar Node-RED

## Comandos útiles

### Verificar puertos

```bash
ss -tulpn | grep :1883  # Puerto MQTT
ss -tulpn | grep :1880  # Puerto Node-RED
```

### Logs de Mosquitto

```bash
sudo journalctl -u mosquitto -f
```
