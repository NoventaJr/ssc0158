sudo apt update
sudo apt install default-jdk

#!/bin/bash

# Update the following variables to match your desired Kafka version and installation directory
KAFKA_HOME="/usr/local/kafka"
KAFKA_VERSION="3.5.0"

# Download Kafka
wget https://downloads.apache.org/kafka/$KAFKA_VERSION/kafka_$KAFKA_VERSION.tgz
tar -xzf kafka_$KAFKA_VERSION.tgz
rm kafka_$KAFKA_VERSION.tgz
mv kafka_$KAFKA_VERSION $KAFKA_HOME

pip3 install paho-mqtt
pip3 install pykafka
pip3 install pymongo

# Start ZooKeeper
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
sleep 5

# Start Kafka broker
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties