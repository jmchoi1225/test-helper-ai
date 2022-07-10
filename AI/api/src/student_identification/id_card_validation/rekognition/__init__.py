import boto3
import json
import sys

from .config import S3_BUCKET_NAME, SIMILARITY_THRESHOLD


def compare_faces(src_path,tar_path):
    src_img = {'S3Object':{'Bucket':S3_BUCKET_NAME,'Name': src_path}}
    tar_img = {'S3Object':{'Bucket':S3_BUCKET_NAME,'Name': tar_path}}
    answer = False
    try :
        client=boto3.client('rekognition')
        response = client.compare_faces(SimilarityThreshold=SIMILARITY_THRESHOLD, SourceImage=src_img, TargetImage=tar_img)
        if len(response['FaceMatches']) > 0 :
            sys.stderr.write("{similarity}\n".format(similarity=response['FaceMatches'][0]['Similarity']))
        answer = len(response['FaceMatches']) > 0
    except :
        sys.stderr.write("AWS connect error! \n")
        answer = False
        
    return answer