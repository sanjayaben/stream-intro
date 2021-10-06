from kafka import KafkaConsumer
import time
import logging

BROKER_URL = "localhost:9092"
TOPIC = "com.sfo.crimes.calls"



consumer = KafkaConsumer(
TOPIC,
bootstrap_servers=[BROKER_URL],
auto_offset_reset='earliest',
group_id='sfo-crime-message-consumer-group')

def run_consumer():
    while(True):
        for message in consumer:
            message = message.value
            print("Received Message ====> ", message)
            time.sleep(1)

        time.sleep(5)

if __name__ == "__main__":
    run_consumer()