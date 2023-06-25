Grupo 14:
 - Carlos Roberto dos Santos Junior - 9435102
 - Rodrigo Noventa Junior - 9791243
 - Leonardo Vinícius de Almeida - 10392230
 - Gabriel dos Reis Coutinho - 9807124


Projeto de Cloud - Instruções para execução:

	0 - É necessário Rodar o script python "./kafka/create_kafka_topics.py" após a execução do kafka broker

	1 - Para a execução do projeto, é necessário ter ao menos 3 abas do terminal abertas.
		1.1 - A primeira aba precisa estar aberta na pasta do projeto - "/gcloud14/mqtt"
		1.2 - A segunda aba precisa estar aberta na pasta do projeto - "/gcloud14/kafka"
		1.3 - A terceira aba precisa estar aberta em "./sensors", aqui poderão ser testado quantos sensores quiser, precisando de uma aba para cada sensor (máximo 4 abas)

	2 - Na aba do terminal aberta em "/gcloud14/mqtt" digitar o comando "python3 bridge.py" então a bridge entre o MQTT e o KAFKA irá ligar e os valores serão postados do MQTT para o KAFKA.
	

	3 - Na segunda aba do terminal em "/gcloud14/kafka" digitar o comando "python3 consumer.py" para começar o consumer do broker kafka. Ele ira receber as mensagens do mqtt

	4 - Na terceira aba "./sensors" para testar cada sensor use o comando "python3 <nome_do_sensor.py>". Lembrando que para cada sensor deve ser aberta uma nova aba no mesmo diretório. Esses sensores irão enviar medidas autogeradas para o MQTT.

	5 - Verificar na primeira aba que a bridge está recebendo os sinais dos sensores. Verificar que na segunda aba o consumer está consumindo os valores dos sensores e armazenando-os em seus respectivos arquivos txt no mesmo diretório do consumer

	(Avançado)

	Para simular a comunicação entre dois dispositivos, podemos executar os sensores em uma das VMs e receber os sinais em outra:
	(por ssh)
	0 - Habilite port forwarding do ssh da porta do kafka da VM1 para a porta do kafka da VM2:
		-`ssh -L 9093:localhost:9092 -p 20123 gcloud14@andromeda.lasdpc.icmc.usp.br`
		0.1 - Execute o script 'install.sh' na pasta do repositório /gcloud14/'
				- dessa vez aperte ctrl c para fechar o kafka broker da VM1
		0.2 - Na maquina navegue até a pasta do repositório e inicie um ou mais sensores:
				- `cd /gcloud14/sensors`
				- `python3 <nome_do_sensor.py>`
				- (Lembrando que cada sensor requer um terminal)
	1 - Inicie o ssh normalmente para a VM2 
		- `ssh -p 20133 gcloud14@andromeda.lasdpc.icmc.usp.br`
	
	2 - Na vm2 inicie a bridge e o consumer:
		2.1 Bridge (em um terminal próprio):
				- navegue para /gcloud/mqtt e execute `python3 bridge.py`
		2.2 Consumer (em um terminal próprio):
				- navegue para /gcloud/mqtt e execute `python3 consumer.py`
	
	3 - Faça as mesmas verificações que o passo 5 acima

