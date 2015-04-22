#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit'))
channel = connection.channel()

channel.exchange_declare(exchange='twitter',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "twitter: Hello World!"
channel.basic_publish(exchange='twitter',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()