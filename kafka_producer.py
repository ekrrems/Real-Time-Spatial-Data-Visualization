from confluent_kafka import Producer

bootstrap_servers = 'localhost:9092'
topic = 'location-topic'

producer_config = {
    'bootstrap.servers': bootstrap_servers
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"Error: {err}")
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')

# for i in range(10):
#     message = f"message number {i}"
#     producer.produce(topic=topic, value=message, callback=delivery_report)

# # Flush the producer to ensure the message is sent
# producer.flush()

def send_kafka_message(message):
    producer.produce(topic=topic, value=message, callback=delivery_report)
    producer.flush()

# bin\windows\kafka-console-producer.bat --bootstrap-server localhost:9092 --topic location-topic