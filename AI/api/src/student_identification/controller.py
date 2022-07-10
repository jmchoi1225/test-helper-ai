from flask_restx import Resource, Namespace
import sys

from .student_number_validation import StudentNumberValidationService
from .id_card_validation import IdCardValidationService

StudentIdentificationNamespace = Namespace(
    name = 'identification',
    description = '학생 본인인증'
)

post_parser = StudentIdentificationNamespace.parser()
post_parser.add_argument('test_id', type= str, location='form', help = 'test_id is required')
post_parser.add_argument('student_num', type= str, location='form', help = 'student_num is required')

@StudentIdentificationNamespace.route("")
class Identification(Resource):
    @StudentIdentificationNamespace.expect(post_parser)
    def post(self):
        args = post_parser.parse_args()

        test_id = args['test_id']
        student_num = args['student_num']

        if not test_id or not student_num :
            sys.stderr.write("no test_id or student_num in request body\n")
            return {'result' : False, 'err_reason' : 'check_request'}


        student_num_result = StudentNumberValidationService().validate_student_number(test_id, student_num)
        if not student_num_result :
            sys.stderr.write("Real student num and student number in id_card do not match!\n")
            return {'result': False, 'err_reason' : 'student_num'}
    
        face_result = IdCardValidationService().validate_id_card(test_id, student_num)
        if not face_result :
            sys.stderr.write("Real student face and student image in id_card do not match!\n")
            return {'result': False, 'err_reason' : 'face'}

        return {'result' : True, 'err_reason': None }
