# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("Temp MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de temperatura
while True:
    randNumber = uniform(30.0, 33.0)
    mqtt_client.publish("Temperatura", f"temperature:{randNumber}")
    print("Temp MQTTProducer " + str(randNumber) + " em Temperatura.")
    time.sleep(3)
