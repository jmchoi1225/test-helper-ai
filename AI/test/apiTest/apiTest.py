import unittest
import json
import warnings
from io import BytesIO
import sys
import cv2

sys.path.extend(["./","../","../../","./src","../src","../../src"])
sys.path.extend(["./AI/src","./AI"])
import app
import s3path

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.student_num = s3path.S3_TEMP_STUDENT_NUM
        self.test_id = s3path.S3_TEMP_TEST_ID
        self.fakestudent_num = '0000000a'
        self.faketest_id = '00000a'
        self.right_parameter = {
            'test_id' : self.test_id,
            'student_num' : self.student_num
        }
        self.wrong_parameter_test_id = {
            'test_id' : self.faketest_id,
            'student_num' : self.student_num
        }
        self.wrong_parameter_student_num= {
            'test_id' : self.test_id,
            'student_num' : self.fakestudent_num
        }
        self.no_parameter_student_num={
            'test_id' : self.test_id
        }
        self.no_parameter_test_id = {
            'student_num' : self.student_num
        }
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

        with open("AI/test/hands/onehand.jpg", 'rb') as img1:
            self.onehand = BytesIO(img1.read())
        with open("AI/test/hands/twohands.jpg", 'rb') as img2:
            self.twohand = BytesIO(img2.read())
        with open("AI/test/hands/fourhands.jpg", 'rb') as img3:
            self.fourhand = BytesIO(img3.read())
        self.wrong = "wrong"

        self.onehand_parameter = {
            'hand_img' : (self.onehand, "onehand.jpg")
        }
        self.twohand_parameter = {
            'hand_img' : (self.twohand, "twohands.jpg")
        }
        self.fourhand_parameter= {
            'hand_img' : (self.fourhand, "fourhands.jpg")
        }
        self.wrong_parameter={
            'hand_img' : self.wrong
        }
        self.no_parameter = {
            'hand_img' : None
        }

    def test_right_identification_parameter(self):
        sys.stderr.write("identification api test\n")
        response = self.app.post('/identification', data=self.right_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(True, data['result'])
        self.assertEqual(None, data['err_reason'])

    def test_wrong_test_parameter(self):
        response = self.app.post("/identification",data=self.wrong_parameter_test_id)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])
        self.assertEqual("student_num", data['err_reason'])

    def test_wrong_studentID_parameter(self):
        response = self.app.post("/identification",data=self.wrong_parameter_student_num)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])
        self.assertEqual("student_num", data['err_reason'])

    def test_no_test_parameter(self):
        response = self.app.post("/identification",data=self.no_parameter_test_id)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])
        self.assertEqual("check_request", data['err_reason'])

    def test_no_studentID_parameter(self):
        response = self.app.post("/identification",data=self.no_parameter_student_num)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False,data['result'])
        self.assertEqual("check_request", data['err_reason'])

    def test_onehand_parameter(self):
        sys.stderr.write("\n\nhand detection api test\n")
        response = self.app.post('/hand-detection', data=self.onehand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_twohand_parameter(self):
        response = self.app.post('/hand-detection', data=self.twohand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(True, data['result'])

    def test_fourhand_parameter(self):
        response = self.app.post('/hand-detection', data=self.fourhand_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_wrong_hand_img_parameter(self):
        response = self.app.post('/hand-detection', data=self.wrong_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

    def test_no_hand_img_parameter(self):
        response = self.app.post('/hand-detection', data=self.no_parameter)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(False, data['result'])

if __name__ == "__main__":
    unittest.main()