import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

#Configurando e conectando MQTT
mqtt_broker = 'mqtt.eclipseprojects.io'
mqqt_client = mqtt.client('MQTTBridge')
mqtt_client.connect(mqtt_broker)

#Configurando e conectando Kafka
kafka_client = KafkaClient(hosts='localhost:9092')
kakfa_topic = kafka_client.topics['temperatura']
kafka_producer = kakfa_topic.get_sync_producer()

#Função para mensagens
def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print('Mensagem recebida de MQTT: ', msg_payload)
    kafka_producer.produce(str(msg_payload).encode('ascii'))
    print('Kafka publicou' + str(msg_payload) + 'em temperatura.')

#Consumindo informações MQTT
mqtt_client.loop_start()
mqtt_client.subscribe('temperatura')
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_stop()