import json
import pika
from pika import connection
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()

from products.models import Product

params = pika.URLParameters(
'amqps://ognssvyy:XSJ7w3QbVynhHveFa__-dIii--nzQYjI@lionfish.rmq.cloudamqp.com/ognssvyy'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()
