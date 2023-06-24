# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqqt_client = mqtt.client("MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de temperatura
while true:
    randNumber = uniform(20.0, 21.0)
    mqtt_client.publish("Temperatura", randNumber)
    print("MQTT publicou" + str(randNumber) + " em temperatura.")
    time.sleep(3)
