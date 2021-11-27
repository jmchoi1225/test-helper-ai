from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS

import sys
sys.path.extend(["./","../","./src","../src"])

from student_identification.detectText import detect_text
from student_identification.compareFace import compare_faces
from hand_detection.yolo import YOLO
import s3path

from PIL import Image
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def index_test():
    return render_template('index.html')

@app.route('/identification',methods=['POST'])
def identification_test():
    test_id = request.form['test_id']
    student_num = request.form['student_num']
    idcard_path= s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num+ s3path.S3_STUDENT_CARD
    face_path = s3path.S3_ROOT+ test_id + s3path.S3_STUDENT_FOLDER+ student_num + s3path.S3_FACE
    bucket=s3path.S3_BUCKET

    if not test_id or not student_num :
        return render_template(
            'result_id.html',
            result = False,
    )

    result_text = detect_text(bucket, idcard_path,student_num)
    
    if not result_text :
        return render_template(
            'result_id.html',
            result = result_text,
    )
    
    result_face = compare_faces(bucket,idcard_path,face_path)
    return render_template(
            'result_id.html',
            result = result_face,
    )



@app.route('/hand-detection',methods=['POST'])
def temp_detection_test():
    hand_img = Image.open(request.files['hand_img'])
    hand_img = cv2.cvtColor(np.array(hand_img), cv2.COLOR_RGB2BGR) 
    width, height, results = detection_model.inference(hand_img)
    conf_sum = 0
    detection_count = 0
    for detection in results:
        id, name, confidence, x, y, w, h = detection
        cx = x + (w / 2)
        cy = y + (h / 2)

        conf_sum += confidence
        detection_count += 1

        # draw a bounding box rectangle and label on the image
        color = (255, 0, 255)
        cv2.rectangle(hand_img, (x, y), (x + w, y + h), color, 3)
        text = "%s (%s)" % (name, round(confidence, 2))
        cv2.putText(hand_img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.25, color, 1)

        print("%s with %s confidence" % (name, round(confidence, 2)))

    cv2.imwrite("static/images/result.jpg", hand_img)
    # opencvImage = cv2.resize(result_image,dsize=(360,240))
    # cv2.imwrite("static/images/result.jpg",opencvImage)
    result_path = "images/result.jpg"
    # # K.clear_session()
    return render_template(
            'result_hand.html', 
            result_path = result_path,
            hand_num=detection_count, 
    )

if __name__ == '__main__':
    detection_model = YOLO("../src/hand_detection/models/yolov4-tiny-custom.cfg","../src/hand_detection/models/yolov4-tiny-custom_only_egodataset.weights", ["hand"])
    app.run(host='0.0.0.0',port=5000,threaded=True, debug=True)
    #app.run(host='0.0.0.0',port=5000,debug=True)