import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

#Configurando e conectando MQTT
mqtt_broker = 'test.mosquitto.org'
mqtt_client = mqtt.Client('MQTTBridge')
mqtt_client.connect(mqtt_broker)

#Configurando e conectando Kafka
kafka_client = KafkaClient(hosts='localhost:9092')
kakfa_topic = kafka_client.topics['Sensors']
kafka_producer = kakfa_topic.get_sync_producer()

#Função para mensagens
def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print('Mensagem recebida de MQTT: ', msg_payload)
    kafka_producer.produce(str(msg_payload).encode('ascii'))
    print('Kafka publicou ' + str(msg_payload) + ' em Sensors.')

#Consumindo informações MQTT
mqtt_client.loop_start()
mqtt_client.subscribe('Sensors')
mqtt_client.on_message = on_message
time.sleep(500)
mqtt_client.loop_stop()