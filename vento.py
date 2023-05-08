#Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

#Configurando e conectando
mqtt_broker = 'mqtt.eclipseprojects.io'
mqqt_client = mqtt.client('MQTTProducer')
mqtt_client.connect(mqtt_broker)

#Simulando publicações de Vento
while true:
    randNumber = uniform(0.0, 20.0)
    mqtt_client.publish("Vento", randNumber)
    print('MQTT publicou' + str(randNumber) + ' em Vento.')
    time.sleep(3)