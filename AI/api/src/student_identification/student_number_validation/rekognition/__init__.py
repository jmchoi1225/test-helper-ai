import boto3
import json
import sys

from .config import S3_BUCKET_NAME


def detect_text(path):
    image = { 'S3Object': { 'Bucket': S3_BUCKET_NAME, 'Name': path } }

    texts = []
    try :
        client=boto3.client('rekognition')
        response = client.detect_text(Image=image)
        for textDetail in response['TextDetections']:
            texts += str(textDetail['DetectedText'])
    except:
        sys.stderr.write("AWS connect error! \n")

    return texts