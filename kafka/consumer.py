from pykafka import KafkaClient
from threading import Thread
import time

# Connect to Kafka
client = KafkaClient(hosts="localhost:9092")

# Define the list of topics to consume from
topics = ["Chuva", "Umidade", "Vento", "Temperatura"]

# Define the output file path
output_files = {topic: topic + ".txt" for topic in topics}


# Consumer function
def consume_messages(topic):
    # Create a consumer for the topic
    consumer = client.topics[topic.encode()].get_simple_consumer()

    # Consume messages and write them to the output file
    with open(output_files[topic], "w") as file:
        for message in consumer:
            if message is not None:
                # Decode the message value assuming it's UTF-8 encoded
                message_value = message.value.decode("utf-8")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(
                    "Topic:", topic, "Message:", message_value, "Timestamp:", timestamp
                )
                # start writing from eof
                file.seek(0, 2)
                file.write(message_value + timestamp + "\n")
                file.flush()  # Flush the buffer to ensure data is written immediately


# Create and start a consumer thread for each topic
consumer_threads = []
for topic in topics:
    thread = Thread(target=consume_messages, args=(topic,))
    thread.start()
    consumer_threads.append(thread)

# Wait for all consumer threads to finish
for thread in consumer_threads:
    thread.join()
