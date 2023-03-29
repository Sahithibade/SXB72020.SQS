import boto3
import logging
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='SQSASSIGNMENT3'
 
 )
print("Created queue '%s' with URL=%s",'myPytonQueue',queue.url)