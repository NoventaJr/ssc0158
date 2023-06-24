# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de umidade
while True:
    randNumber = uniform(80.0, 90.0)
    mqtt_client.publish("Umidade", f"Umidade:{randNumber}")
    print("MQTT publicou " + str(randNumber) + " em Umidade.")
    time.sleep(3)
