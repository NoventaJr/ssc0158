# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de Chuva
while True:
    randNumber = uniform(0.0, 10.0)
    mqtt_client.publish("Chuva", f"Chuva:{randNumber}")
    print("MQTT publicou" + str(randNumber) + " em Chuva.")
    time.sleep(3.0)
