sudo apt update
sudo apt install default-jdk

wget https://downloads.apache.org/kafka/3.5.0/kafka_2.12-3.5.0.tgz

tar xzf kafka_2.13-3.4.0.tgz
sudo mv kafka_2.13-3.4.0 /usr/local/kafka 

pip3 install paho-mqtt
pip3 install pykafka
pip3 install pymongo

python3 ./kafka/create_kafka_topics.py