###### Start ZooKeeper ##############
cd apache-zookeeper-3.7.0-bin
sudo bin/zkServer.sh start
sudo bin/zkServer.sh stop

###### Start Kafka ##############
cd kafka_2.12-3.0.0/
bin/kafka-server-start.sh config/server.properties
bin/kafka-server-stop.sh config/server.properties