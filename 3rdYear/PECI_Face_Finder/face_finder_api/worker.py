import pika
import json
import asyncio
from services.FaceRecognitionService import FaceRecognitionService

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
    message = json.loads(body)
    albumId = message['albumId']
    imageKeyList = message['imageKeyList']
    currentUser = message['currentUser']

    faceRecognitionService = FaceRecognitionService()  # Initialize your service
    asyncio.run(faceRecognitionService.face_recog_alg(albumId, imageKeyList, currentUser))

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, heartbeat=600))
channel = connection.channel()
channel.queue_declare(queue='face_recognition')
channel.basic_consume(queue='face_recognition', on_message_callback=callback, auto_ack=True)
channel.start_consuming()