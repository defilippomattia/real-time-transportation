from kafka import KafkaProducer
import json
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:29092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
f = open('route-1.json')
my_route = json.load(f)
gps_coordinates = my_route["features"][0]["geometry"]["coordinates"][0]
#print(gps_coordinates)

for point in gps_coordinates:
    #producer.send('sample', b'Hello, World!')
    #producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
    producer.send('sample', key=b'message-two', value=point)
    producer.flush()
    sleep(5)

#     print(point)
#     producer.send('points',b'fdfd')
#     producer.flush()

#     sleep(1)


# producer.send('points',b'fdfd')
# for i in range(0,10):
#     producer.send('sample', b'aaaaa')
# producer.flush()