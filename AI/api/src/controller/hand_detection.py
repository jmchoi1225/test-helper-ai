from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage

import numpy as np
import cv2
import sys

from ai.hand_detection.src.yolo import YOLO

HandDetectionNamespace = Namespace(
    name = 'hand-detection',
    description = '학생의 두 손이 화면 안에 있는지 확인'
)

post_parser = HandDetectionNamespace.parser()
post_parser.add_argument('hand_img', type = FileStorage, location = 'files', help = 'hand_img is required')

detection_model = YOLO("ai/hand_detection/src/yolo/v4-tiny-custom.cfg","ai/hand_detection/src/yolo/v4-tiny.weights", ["hand"])

@HandDetectionNamespace.route('')
class HandDetectionController(Resource):
    @HandDetectionNamespace.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()
        try :
            hand_img = args['hand_img'].read()
            hand_img = cv2.imdecode(np.fromstring(hand_img, np.uint8), cv2.IMREAD_UNCHANGED)
        except :
            sys.stderr.write("no hand_img in request body\n")
            return {'result' : False}

        try :
            width, height, results = detection_model.inference(hand_img)
            hand_num = len(results)
            sys.stderr.write("hand_num : {hand_num}\n".format(hand_num=hand_num))
        except Exception as e:
            sys.stderr.write("error to detection\n")
            return {'result':False}

        return {'result': hand_num == 2}