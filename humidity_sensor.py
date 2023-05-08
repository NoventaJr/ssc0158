#Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

#Configurando e conectando
mqtt_broker = 'test.mosquitto.org'
mqtt_client = mqtt.Client('MQTTProducer')
mqtt_client.connect(mqtt_broker)

#Simulando publicações de humidade
while True:
    randNumber = uniform(20.0, 21.0)
    mqtt_client.publish("Sensors", f"humidity:{randNumber}")
    print('MQTT publicou ' + str(randNumber) + ' de humidade em Sensors.')
    time.sleep(3)