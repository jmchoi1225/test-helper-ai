from flask_restx import Resource, Namespace
import sys

import rekognition_config as s3path
from ai.face_compare.src.rekognition import compare_faces
from ai.text_detection.src.rekognition import detect_text

IdentificationNamespace = Namespace(
    name = 'identification',
    description = '학생 본인인증'
)

post_parser = IdentificationNamespace.parser()
post_parser.add_argument('test_id', type= str, location='form', help = 'test_id is required')
post_parser.add_argument('student_num', type= str, location='form', help = 'student_num is required')

@IdentificationNamespace.route("")
class Identification(Resource):
    @IdentificationNamespace.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()

        test_id = args['test_id']
        student_num = args['student_num']

        if not test_id or not student_num :
            sys.stderr.write("no test_id or student_num in request body\n")
            return {'result' : False, 'err_reason' : 'check_request'}

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
