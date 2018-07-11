"""
Simple example for Lambda->SQS->Lambda.
"""

import os
import boto3

SQS_CLIENT = boto3.client('sqs')


def start(event, context):
    """
    First Lambda function. Triggered manually.
    :param event: AWS event data
    :param context: AWS function's context
    :return: ''
    """
    print(SQS_CLIENT.send_message(
        QueueUrl=os.getenv('SQS_URL'),
        MessageBody='test'
    ))
    return ''


def end(event, context):
    """
    Second Lambda function. Triggered by the SQS.
    :param event: AWS event data (this time will be the SQS's data)
    :param context: AWS function's context
    :return: ''
    """
    print(event)
    return ''
