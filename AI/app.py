from student_identification.detectText import detect_text
from student_identification.compareFace import compare_faces

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, redirect, url_for, request, render_template
from flask_restful import reqparse
from flask_cors import CORS

import json
import os

app = Flask(__name__)
CORS(app)


@app.route('/identification',methods=['POST'])
def identification():
    parser = reqparse.RequestParser()
    parser.add_argument('test_id')
    parser.add_argument('student_id')
    args = parser.parse_args()

    test_id = args['test_id']
    student_id = args['student_id']
    
    if not test_id or not student_id :
        print("no test_id or student_id")
        return json.dumps({'result' : False})

    idcard_path="test/" + test_id + "/submission/" + student_id + "/student_card.jpg"
    face_path = "test/"  + test_id + "/submission/" + student_id + "/face.jpg"
    bucket="testhelper"


    result_text = False
    try : 
        result_text = detect_text(bucket, idcard_path,student_id)
    except :
        print("AWS 에 접근 시 오류가 발생하였습니다! ")
        return json.dumps({'result': False})
    
    if not result_text :
        return json.dumps({'result': False})

    result_face = False
    try :
        result_face =compare_faces(bucket,idcard_path,face_path)
    except :
        print("AWS 에 접근 시 오류가 발생하였습니다! ")
        return json.dumps({'result' : False})
        
    return json.dumps({'result' : result_face})



@app.route('/hand-detection',methods=['POST'])
def detection():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)