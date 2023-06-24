import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

# Configurando e conectando MQTT
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("MQTTBridge")
mqtt_client.connect(mqtt_broker)

# Configurando e conectando Kafka
kafka_client = KafkaClient(hosts="localhost:9092")

# Topics
kafka_temp_topic = kafka_client.topics[b"Temperatura"]
kafka_wind_topic = kafka_client.topics[b"Vento"]
kafka_hum_topic = kafka_client.topics[b"Umidade"]
kafka_rain_topic = kafka_client.topics[b"Chuva"]

# Producers
kafka_temp_producer = kafka_temp_topic.get_sync_producer()
kafka_wind_producer = kafka_wind_topic.get_sync_producer()
kafka_hum_producer = kafka_hum_topic.get_sync_producer()
kafka_rain_producer = kafka_rain_topic.get_sync_producer()


# Função para mensagens
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")

    if topic == "Temperatura":
        kafka_temp_producer.produce(payload.encode("ascii"))
        print("Mensagem publicada em Temperatura no Kafka.")
    elif topic == "Vento":
        kafka_wind_producer.produce(payload.encode("ascii"))
        print("Mensagem publicada em Vento no Kafka.")
    elif topic == "Umidade":
        kafka_hum_producer.produce(payload.encode("ascii"))
        print("Mensagem publicada em Umidade no Kafka.")
    elif topic == "Chuva":
        kafka_rain_producer.produce(payload.encode("ascii"))
        print("Mensagem publicada em Chuva no Kafka.")


# Consumindo informações MQTT
mqtt_client.loop_start()

topics = [("Temperatura", 0), ("Vento", 0), ("Umidade", 0), ("Chuva", 0)]

mqtt_client.subscribe(topics)
mqtt_client.on_message = on_message
mqtt_client.loop_stop()
