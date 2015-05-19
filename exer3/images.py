#!/usr/bin/env python
import pika
import re


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit'))
channel = connection.channel()

channel.exchange_declare(exchange='twitter',
                         type='fanout')
						 
queue_name = "images"
result = channel.queue_declare(queue=queue_name, exclusive=True)

channel.queue_bind(exchange='twitter',
                   queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

picture = re.compile("\w+\.(jpg|png)")
# tag = re.compile("#.*#")
def callback(ch, method, properties, twitter):
    print "twitter [x] %r" % (twitter,)
    if picture.search(twitter):
        print "==> find picture, start processing ..."

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()