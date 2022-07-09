import boto3
import json
import sys


def detect_text(bucket,path,studentNum):
    image = {'S3Object':{'Bucket':bucket,'Name':path}}
    correct = False 
    try :
        client=boto3.client('rekognition')
        response = client.detect_text(Image=image) 
        for textDetail in response['TextDetections']:
            # print(json.dumps(textDetail, indent=4, sort_keys=True))
            if studentNum == str(textDetail['DetectedText']) :
                correct= True
                break
    except:
        sys.stderr.write("AWS connect error! \n")
        return False

    return correct