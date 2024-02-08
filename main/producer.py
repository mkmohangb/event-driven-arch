import pika
from pika import connection
import json

params = pika.URLParameters(
'amqps://ognssvyy:XSJ7w3QbVynhHveFa__-dIii--nzQYjI@lionfish.rmq.cloudamqp.com/ognssvyy'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body),
                          properties=properties)

