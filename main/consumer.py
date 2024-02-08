import pika
from pika import connection
import json
from main import Product, db

params = pika.URLParameters(
'amqps://ognssvyy:XSJ7w3QbVynhHveFa__-dIii--nzQYjI@lionfish.rmq.cloudamqp.com/ognssvyy'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'],
                          image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product created')
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        if product != None:
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted')
        else:
            print('Product not found')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()
