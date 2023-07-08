from confluent_kafka import Producer

bootstrap_servers = 'localhost:9092'
topic = 'location_data'

producer_config = {
    'bootstrap.servers': bootstrap_servers
}

producer = Producer(producer_config)

message_value = 'Hello, Kafka!'
message_key = 'your_key'  # Optional: specify a key for message partitioning

producer.produce(topic=topic, value=message_value, key=message_key)

# Flush the producer to ensure the message is sent
producer.flush()

producer.close()