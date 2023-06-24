from pykafka import KafkaClient

# Connect to Kafka
client = KafkaClient(hosts="localhost:9092")

# Define the list of topics to consume from
topics = ["Chuva", "Umidade", "Vento", "Temperatura"]

# Create a consumer
consumer = client.topics[[topic.encode() for topic in topics]].get_simple_consumer(
    consumer_group=b"your_consumer_group"
)

# Define the output file paths
output_files = {topic: topic + ".txt" for topic in topics}

# Consume messages and write them to the output files
for message in consumer:
    if message is not None:
        topic = message.topic.decode()
        file = open(output_files[topic], "a")
        # Decode the message value assuming it's UTF-8 encoded
        message_value = message.value.decode("utf-8")
        print("Topic:", topic, "Message:", message_value)
        file.write(message_value + "\n")
        file.flush()  # Flush the buffer to ensure data is written immediately
