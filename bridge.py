import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

# Configuring and connecting MQTT
mqtt_broker = "test.mosquitto.org"
mqtt_client = mqtt.Client("MQTTBridge")
mqtt_client.connect(mqtt_broker)

# Configuring and connecting Kafka
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


# Function to handle MQTT messages
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")

    print("Received message from MQTT - Topic:", topic)
    print("Received message from MQTT - Payload:", payload)

    if "Temperatura" in topic:
        kafka_temp_producer.produce(payload.encode("ascii"))
        print("Message published to Temperatura topic in Kafka.")
    elif "Vento" in topic:
        kafka_wind_producer.produce(payload.encode("ascii"))
        print("Message published to Vento topic in Kafka.")
    elif "Umidade" in topic:
        kafka_hum_producer.produce(payload.encode("ascii"))
        print("Message published to Umidade topic in Kafka.")
    elif "Chuva" in topic:
        kafka_rain_producer.produce(payload.encode("ascii"))
        print("Message published to Chuva topic in Kafka.")


# Subscribing to MQTT topics
mqtt_client.on_message = on_message

mqtt_client.subscribe(
    "+/+", qos=0
)  # Single-level wildcard: "+/+" matches any single-level topic

# Consuming MQTT messages
mqtt_client.loop_start()

time.sleep(500)

mqtt_client.loop_stop()
