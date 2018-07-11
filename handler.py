"""
Simple example for Lambda->SQS->Lambda.
"""

import boto3

SQS_CLIENT = boto3.client('sqs')
SQS_URL = 'https://sqs.<region>.amazonaws.com/<account>/TutorialSQS'


def start(_event, _context):
    """
    First Lambda function. Triggered manually.
    :param _event: AWS event data
    :param _context: AWS function's context
    :return: ''
    """
    print(SQS_CLIENT.send_message(
        QueueUrl=SQS_URL,
        MessageBody='test'
    ))
    return ''


def end(event, _context):
    """
    Second Lambda function. Triggered by the SQS.
    :param event: AWS event data (this time will be the SQS's data)
    :param _context: AWS function's context
    :return: ''
    """
    print(event)
    return ''
