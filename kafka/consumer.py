from pykafka import KafkaClient

# Connect to Kafka
client = KafkaClient(hosts="localhost:9092")

# Choose the topic to consume from
topic_name = "Umidade"

# Create a consumer
consumer = client.topics[
    "Chuva".encode(), "Umidade".encode(), "Vento".encode(), "Temperatura".encode()
].get_simple_consumer()

# Define the output file path
output_file = "medidas.txt"

# Consume messages and write them to the output file
for message in consumer:
    if message is not None:
        file = open(message.topic, "a")
        # Decode the message value assuming it's UTF-8 encoded
        message_value = message.value.decode("utf-8")
        print(message_value, "\n")
        file.write(message_value + "\n")
        file.flush()  # Flush the buffer to ensure data is written immediately
