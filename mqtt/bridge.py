import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time
from threading import Thread


class MQTTBridge:
    def __init__(self, mqtt_broker, kafka_broker):
        self.mqtt_broker = mqtt_broker
        self.kafka_client = KafkaClient(hosts=kafka_broker)

    def bridge_mqtt_to_kafka(self, mqtt_topic, kafka_topic):
        mqtt_client = mqtt.Client()
        mqtt_client.connect(self.mqtt_broker)

        kafka_topic = self.kafka_client.topics[kafka_topic]
        kafka_producer = kafka_topic.get_sync_producer()

        def on_message(client, userdata, message):
            mqtt_topic = message.topic
            payload = message.payload.decode("utf-8")

            print("Received MQTT message from topic:", mqtt_topic)
            print("Publishing to Kafka topic:", kafka_topic)

            kafka_producer.produce(payload.encode("ascii"))

        mqtt_client.on_message = on_message
        mqtt_client.subscribe(mqtt_topic)
        mqtt_client.loop_start()

    def start_bridge(self):
        mqtt_to_kafka_threads = [
            Thread(
                target=self.bridge_mqtt_to_kafka,
                args=(mqtt_topic, kafka_topic),
            )
            for mqtt_topic, kafka_topic in self.mqtt_to_kafka_mappings
        ]

        for thread in mqtt_to_kafka_threads:
            thread.start()

        time.sleep(500)

        for thread in mqtt_to_kafka_threads:
            thread.join()


# Configuring MQTT broker, Kafka broker, and MQTT to Kafka topic mappings
mqtt_broker = "test.mosquitto.org"
kafka_broker = "localhost:9092"
mqtt_to_kafka_mappings = [
    ("Temperatura", "Temperatura"),
    ("Vento", "Vento"),
    ("Umidade", "Umidade"),
    ("Chuva", "Chuva"),
]

# Creating MQTTBridge instance
mqtt_bridge = MQTTBridge(mqtt_broker, kafka_broker)
mqtt_bridge.mqtt_to_kafka_mappings = mqtt_to_kafka_mappings

# Starting the MQTT to Kafka bridge
mqtt_bridge.start_bridge()
