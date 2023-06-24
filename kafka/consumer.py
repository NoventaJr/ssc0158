from pykafka import KafkaClient

# Connect to Kafka
client = KafkaClient(hosts="localhost:9092")

# Define the list of topics to consume from
topics = ["Chuva", "Umidade", "Vento", "Temperatura"]

# Create a consumer
consumer = client.topics[[topic.encode() for topic in topics]].get_simple_consumer()

# Define the output file path
output_file = "medidas.txt"

# Consume messages and write them to the output file
for message in consumer:
    if message is not None:
        file = open(message.topic.decode() + ".txt", "a")
        # Decode the message value assuming it's UTF-8 encoded
        message_value = message.value.decode("utf-8")
        print(message_value, "\n")
        file.write(message_value + "\n")
        file.flush()  # Flush the buffer to ensure data is written immediately
