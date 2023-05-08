Grupo 14:
 - Carlos Roberto dos Santos Junior - 9435102
 - Rodrigo Noventa Junior - 9791243
 - Leonardo Vinıcius de Almeida - 10392230
 - Gabriel dos Reis Coutinho - 9807124


Projeto de Cloud - Instruções para executação:

	1 - Para a execução do projeto, é necessário ter 3 abas do terminal abertas.
		1.1 - A primeira aba precisa estar aberta na pasta do projeto - "./scc0158/"
		1.2 - A segunda aba precisa estar aberta na pasta do projeto - "./scc0158/"
		1.3 - A terceira aba precisa estar aberta em "/usr/local/kafka/bin"
			1.3.1 - Para isto basta digitar o comando "cd /usr/local/kafka/bin"

	2 - Na primeira aba do terminal digitar o comando "python3 temp_sensor.py" então o simulador de temperatura irá começar a rodar, postando os valores simulados no MQTT.

	3 - Na segunda aba do terminal digitar o comando "python3 bridge.py" então a bridge entre o MQTT e o KAFKA irá ligar e os valores serão postados do MQTT para o KAFKA.

	4 - Na terceira aba digitar o comando "kafka-topics.sh --create --topic Sensors --bootstrap-server localhost:9092" será então criado o tópico dos sensores, então o kafka poderá começar a pegar os valores

	5 - Na terceira aba digitar o comando "kafka-console-consumer.sh --topic Sensors --from-beginning --bootstrap-server localhost:9092" então o consumidor do kafta iniciará e consumirá os valores do recebidos do MQTT.