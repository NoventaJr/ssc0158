# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de temperatura
while True:
    randNumber = uniform(30.0, 33.0)
    mqtt_client.publish("Temperatura", f"temperature:{randNumber}")
    print("MQTT publicou " + str(randNumber) + " em Temperatura.")
    time.sleep(1.5)
