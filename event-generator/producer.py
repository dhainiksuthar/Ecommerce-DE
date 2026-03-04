from kafka import KafkaProducer
import json

KAFKA_BOOTSTRAP_SERVERS = ['kafka:9093']

# Topic names
CLICKSTREAM_TOPIC = "clickstream"
ORDERS_TOPIC = "orders"
INVENTORY_TOPIC = "inventory"

producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None,
            retries=5,
            retry_backoff_ms=1000,
            acks='all',
        )
print(f"Connected to Kafka: {KAFKA_BOOTSTRAP_SERVERS}")

producer.send(CLICKSTREAM_TOPIC, value="Val", key="key")