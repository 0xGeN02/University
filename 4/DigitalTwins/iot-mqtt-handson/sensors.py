import paho.mqtt.client as mqtt
import time, random

# Conexión al broker
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect("localhost", 1883, 60)

while True:
    temp = round(random.uniform(20, 30), 2)   # genera temperatura aleatoria
    hum = round(random.uniform(40, 60), 2)    # genera humedad aleatoria

    client.publish("casa/salon/temperatura", temp)
    client.publish("casa/salon/humedad", hum)

    print(f"Publicado -> Temp:{temp}°C  Hum:{hum}%")
    time.sleep(2)
