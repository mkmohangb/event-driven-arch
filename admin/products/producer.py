import pika
from pika import connection
import json

params = pika.URLParameters(
'amqps://wavyywnp:NwTeeH1bsUyOPHhGNPA9CARMLN14ksd5@lionfish.rmq.cloudamqp.com/wavyywnp'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body),
                          properties=properties)

