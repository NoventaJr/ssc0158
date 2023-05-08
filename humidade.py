#Importando biblioteca do cliente MQTT e auxiliares
import paho.mqtt.client as mqtt
from random import uniform
import time

#Configurando e conectando
mqtt_broker = 'mqtt.eclipseprojects.io'
mqqt_client = mqtt.client('MQTTProducer')
mqtt_client.connect(mqtt_broker)

#Simulando publicações de Humidade
while true:
    randNumber = uniform(50.0, 80.0)
    mqtt_client.publish("Humidade", randNumber)
    print('MQTT publicou' + str(randNumber) + ' em Humidade.')
    time.sleep(3)