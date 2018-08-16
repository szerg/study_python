import pika
import sys
import time
import json
from random import randint

import logging

class MessagePublisher(object):
    connected = False

    def __init__(self, config, logger = None):

        self.logger = logger
        self._connection = None
        self._channel = None
        self.exchange = config.get('rmq-message-exchange', None)
        self.amqp_url = config.get('amqp_url', None)
        self.reconnection_timeout = 0

        self.connect()

    def connect(self):
        connected = False
        try:
            self._connection = pika.BlockingConnection(
                    pika.URLParameters(self.amqp_url)
                )
            self._channel = self._connection.channel()
            connected = True
        except pika.exceptions.AMQPChannelError as e:
            self.logger.error("Got a channel error while trying to connect! %s" % e)
            connected = False
        except Exception as e:
            self.logger.error("Got an exception! %s" % e)
            connected = False

    def publish_message(self, routing_key, message, priority = 0):
        """This method publishes a message with the specified routing_key"""
        try:
            self._channel.basic_publish(
                exchange = self.exchange,
                routing_key = routing_key,
                body = message,
                properties=pika.BasicProperties(
                    delivery_mode = 2, # make message persistent
                    priority = priority, #set the priority for the queue
                )
            )

            self.reconnection_timeout = 0
        except Exception as ex:
            self.logger.error(ex)
            self.logger.info(
                "Publishing failed... Reconnecting in %d seconds..." %
                self.reconnection_timeout
            )
            time.sleep(self.reconnection_timeout)

            '''
            reconnection timeout should be bounded to 5 minutes
            also, add a random delta so that not all workers
            reconnect at the same time
            '''
            self.reconnection_timeout = min(
                pow(
                    self.reconnection_timeout + 1,
                    2
                ),
                300
            ) + randint(0, 30)
            self.connect()
            self.publish_message(
                routing_key,
                message,
                priority
            )




config = {}
config['rmq-message-queue'] = "scan_fetched_multiav"
config['rmq-message-exchange'] = "exchangeRabbitDevTest"
config['rmq-exchangetype'] = "direct"
config['rmq-exchange-durable'] = True
config['rmq-queue-durable'] = True
config['rmq-message-routingkey'] = "scan_fetched"
config['rmq-max-priority'] = 1
config['logger'] = "thisLogger"
#config['amqp_url'] = "http://admin:adm1n@10.38.182.99:15672/api/vhosts/"   ?connection_attempts=5&socket_timeout=5&heartbeat=2&retry_delay=1

#config['amqp_url'] = "amqp://guest:guest@ec2-18-188-123-189.us-east-2.compute.amazonaws.com:5672/?connection_attempts=5&socket_timeout=5&retry_delay=1"
config['amqp_url'] = "amqp://guest:guest@18.188.123.189:5672/?connection_attempts=5&socket_timeout=5&retry_delay=1"
#config['amqp_url'] = "amqp://admin:adm1n@18.188.123.189:5672/?connection_attempts=5&socket_timeout=5&heartbeat=2&retry_delay=1"
#config['amqp_url'] = "amqp://guest:guest@rabbit.ro.dev.rap.atirc.int:5672/?connection_attempts=5&socket_timeout=5&heartbeat=2&retry_delay=1"

if __name__ =="__main__":
    print(config)
    publisher = MessagePublisher(
        config,
        logging
    )

    print publisher.connected
    '''
    if publisher.connected:
        batch =[]
        for i in range(10):
            message = "Some message ... "+str(time.ctime())+" "+str(i)
            #batch.append(record)
            publisher.publish_message("scan_fetched", message, randint(0,4))
            print("Sent message: "+message+ "===>   Waiting 2 seconds...")
            time.sleep(2)
    '''
    print("Completed!")
