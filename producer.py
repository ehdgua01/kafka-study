from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
future = producer.send("example", b"hello world")
future.get(10)
