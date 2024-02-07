import pika
from pika import connection

params = pika.URLParameters(
'amqps://wavyywnp:NwTeeH1bsUyOPHhGNPA9CARMLN14ksd5@lionfish.rmq.cloudamqp.com/wavyywnp'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()
