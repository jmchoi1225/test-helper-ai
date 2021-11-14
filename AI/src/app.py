from flask import Flask
from flask_restful import reqparse
from flask_cors import CORS
from flask_restx import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage

import sys
sys.path.extend(["../","./","./AI"])
import json
from PIL import Image
import numpy as np
import cv2

from student_identification.detectText import detect_text
from student_identification.compareFace import compare_faces
from hand_detection.google_hand import google_hands
import s3path

app = Flask(__name__)
# app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

api = Api(app,versison='1.0',title='test-helper-ai-api',
          description = 'check test-helper-ai-api')
ns_identification = api.namespace('identification', description = 'student identification')
ns_hand_detection = api.namespace('hand-detection',description= "hand detection")

parser_identification = api.parser()
parser_identification.add_argument('test_id', type= str,help = 'ID of test',required=True, location='form')
parser_identification.add_argument('student_num', type= str,help = 'num of student',required=True, location='form')

parser_hand = api.parser()
parser_hand.add_argument('hand_img', type =FileStorage, help = "hand image",required=True, location='files')

@ns_identification.route("")
class Identification(Resource):
    @api.expect(parser_identification)
    def post(self):
        args = parser_identification.parse_args()

        test_id = args['test_id']
        student_num = args['student_num']

        if not test_id or not student_num :
            sys.stderr.write("no test_id or student_num in request body\n")
            return {'result' : False,
                            'err_reason' : 'check_request'}

        idcard_path= s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_STUDENT_CARD
        face_path = s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_FACE
        bucket=s3path.S3_BUCKET
        sys.stderr.write("idcard_path : {idcard_path}\n".format(idcard_path=idcard_path))
        sys.stderr.write("face_path : {face_path}\n".format(face_path=face_path))

        result_text = detect_text(bucket, idcard_path,student_num)
        if not result_text :
            sys.stderr.write("Real student num and student number in id_card do not match!\n")
            return {'result': False,
                               'err_reason' : 'student_num'}
    
        result_face = compare_faces(bucket,idcard_path,face_path)
        if not result_face :
            sys.stderr.write("Real student face and student image in id_card do not match!\n")
            return {'result': False,
                               'err_reason' : 'face'}
        return {'result' : result_face,
                           'err_reason': None }


@ns_hand_detection.route("")
class HandDetection(Resource):
    @api.expect(parser_hand)
    def post(self):
        args = parser_hand.parse_args()
        hand_img = Image.open(args['hand_img'])
        try :
            hand_num = google_hands(cv2.cvtColor(np.array(hand_img), cv2.COLOR_RGB2BGR))
        # hand_num = yolo.detect_image(image)
        except :
            sys.stderr.write("mediapipe error(because of no hand i think)")
            return {'result':False}
        result=False
        if hand_num == 2 :
            result = True
   
        # K.clear_session()
        return {'result':result}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)