from pykafka import KafkaClient

import json

# start a consumer on the topics: Temperatura Vento Umidade Chuva
consumer = (
    KafkaClient(hosts="localhost:9092")
    .topics[b"Temperatura", b"Vento", b"Umidade", b"Chuva"]
    .get_simple_consumer()
)

# Parse received data from Kafka
for msg in consumer:
    # Create dictionary and ingest data into MongoDB
    try:
        print("Data recovered by kafka", msg)
    except Exception as e:
        print("error consuming", str(e))
