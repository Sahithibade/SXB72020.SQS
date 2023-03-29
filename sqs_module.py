import boto3

# Set up the SQS client
sqs = boto3.client('sqs')

# Create the queue
response = sqs.create_queue(
    QueueName='my-queue',
)

# Get the queue URL from the response
queue_url = response['QueueUrl']

# Send a message to the queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello, world!'
)

# Process messages in the queue
with open('output.txt', 'w') as file:
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            VisibilityTimeout=0,
            WaitTimeSeconds=20,
        )

        if 'Messages' not in response:
            print('Queue is empty')
            break

        message = response['Messages'][0]
        print('Received message:', message['Body'])
        file.write(message['Body'] + '\n')

        # Process the message here

        # Delete the message from the queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
