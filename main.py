import boto3
import logging
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='sqs_module'
 
 )
print("Created queue '%s' with URL=%s",'sqs_module',queue.url)