# Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

# Configurando e conectando
mqtt_broker = "test.mosquitto.org"
mqqt_client = mqtt.client("Vento MQTTProducer")
mqtt_client.connect(mqtt_broker)

# Simulando publicações de Vento
while true:
    randNumber = uniform(0.0, 5.0)
    mqtt_client.publish("Vento", f"Vento:{randNumber}")
    print("Vento MQTTProducer " + str(randNumber) + " em Vento.")
    time.sleep(3)
