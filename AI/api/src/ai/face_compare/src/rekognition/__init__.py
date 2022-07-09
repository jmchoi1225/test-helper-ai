import boto3
import json
import sys


def compare_faces(bucket,src_path,tar_path):
    SIMILARITY_THRESHOLD = 75
    src_img = {'S3Object':{'Bucket':bucket,'Name': src_path}}
    tar_img = {'S3Object':{'Bucket':bucket,'Name': tar_path}}
    answer = True
    try :
        client=boto3.client('rekognition')
        response = client.compare_faces(SimilarityThreshold=SIMILARITY_THRESHOLD, SourceImage=src_img, TargetImage=tar_img)
        if len(response['FaceMatches'])==0 :
            answer=False
        else :
            sys.stderr.write("{similarity}\n".format(similarity=response['FaceMatches'][0]['Similarity']))
    except :
        sys.stderr.write("AWS connect error! \n")
        return False
        
    return answer