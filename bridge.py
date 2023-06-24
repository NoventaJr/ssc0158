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
kafka_hum_topic = kafka_hum_topic.get_sync_producer()
kafka_rain_topic = kafka_rain_topic.get_sync_producer()


# Função para mensagens
def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print("Mensagem raw recebida de MQTT:", message)
    print("Mensagem recebida de MQTT:", msg_payload)

    kafka_temp_producer.produce(msg_payload.encode("ascii"))
    kafka_wind_producer.produce(msg_payload.encode("ascii"))
    kafka_hum_topic.produce(msg_payload.encode("ascii"))
    kafka_rain_topic.produce(msg_payload.encode("ascii"))

    print("Kafka publicou", msg_payload, "em Sensors.")
    print("Kafka publicou", msg_payload, "em Sensors.")
    print("Kafka publicou", msg_payload, "em Sensors.")
    print("Kafka publicou", msg_payload, "em Sensors.")


# Consumindo informações MQTT
mqtt_client.loop_start()

topics = [("Temperatura", 0), ("Vento", 0), ("Umidade", 0), ("Chuva", 0)]

mqtt_client.subscribe(topics)
mqtt_client.on_message = on_message

time.sleep(500)

mqtt_client.loop_stop()
