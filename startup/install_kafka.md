# Installing Kafka
## Linux/MacOS
### Install Zookeeper 
`cd /opt/`  
`sudo wget https://dlcdn.apache.org/zookeeper/zookeeper-3.7.0/apache-zookeeper-3.7.0-bin.tar.gz`  
`sudo tar -xzvf apache-zookeeper-3.7.0-bin.tar.gz`  
`sudo rm apache-zookeeper-3.7.0-bin.tar.gz`  
`cd apache-zookeeper-3.7.0-bin`  
`sudo mv conf/zoo_sample.cfg conf/zoo.cfg`  


### Install Kafka 
`cd /opt/`  
`sudo wget https://archive.apache.org/dist/kafka/3.0.0/kafka_2.12-3.0.0.tgz`  
`sudo tar -xzvf kafka_2.12-3.0.0.tgz`  
`sudo rm kafka_2.12-3.0.0.tgz`  

## Windows
Please follow https://www.goavega.com/install-apache-kafka-on-windows/






