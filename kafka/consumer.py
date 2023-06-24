from pykafka import KafkaClient

# Connect to Kafka
client = KafkaClient(hosts="localhost:9092")

# Choose the topic to consume from
topic_name = "your_topic_name"

# Create a consumer
consumer = client.topics[topic_name.encode()].get_simple_consumer()

# Define the output file path
output_file = "output.txt"

# Consume messages and write them to the output file
with open(output_file, "w") as file:
    for message in consumer:
        if message is not None:
            # Decode the message value assuming it's UTF-8 encoded
            message_value = message.value.decode("utf-8")
            file.write(message_value + "\n")
            file.flush()  # Flush the buffer to ensure data is written immediately
