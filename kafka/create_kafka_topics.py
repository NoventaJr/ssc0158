from pykafka import KafkaClient


# Function to create a list of Kafka topics from a text file
def create_topic_list_from_file(file_path):
    topic_list = []
    with open(file_path, "r") as file:
        for line in file:
            topic = line.strip()  # Remove leading/trailing whitespace
            if topic:
                topic_list.append(topic)
    return topic_list


# Example usage
if __name__ == "__main__":
    file_path = "kafka-topics.txt"  # Replace with your file path
    kafka_host = "localhost:9092"  # Replace with your Kafka host address

    # Create the Kafka client
    client = KafkaClient(hosts=kafka_host)

    # Read topics from the file
    topics = create_topic_list_from_file(file_path)

    # Create Kafka topics
    for topic in topics:
        client.create_topic(topic, num_partitions=1, replication_factor=1)

    print("Topics created successfully!")
