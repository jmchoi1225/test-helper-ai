import unittest
import cv2
import sys
sys.path.extend(["./","../","../../","./src","../src","../../src"])
sys.path.extend(["./AI/src","./AI"])
from hand_detection.yolo import YOLO

class UnitTest(unittest.TestCase):
    def setUp(self): 
        self.detection_model = YOLO("AI/src/hand_detection/models/yolov4-tiny-custom.cfg","AI/src/hand_detection/models/yolov4-tiny-custom_only_egodataset.weights", ["hand"])
        self.fourhands = cv2.imread("AI/test/hands/fourhands.jpg")
        self.twohands = cv2.imread("AI/test/hands/twohands.jpg")
        self.onehand = cv2.imread("AI/test/hands/onehand.jpg")

    def test_four_hands(self):
        width, height, results = self.detection_model.inference(self.fourhands)
        self.assertEqual(4,len(results))

    def test_two_hands(self):
        width, height, results = self.detection_model.inference(self.twohands)
        self.assertEqual(2,len(results))

    def test_one_hand(self):
        width, height, results = self.detection_model.inference(self.onehand)
        self.assertEqual(1,len(results))


if __name__ == '__main__':
    unittest.main()