from .yolo import YOLO

class HandDetectionService:
    def __new__(cls): # singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(HandDetectionService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.model = YOLO("hand_detection/ai/yolo/v4-tiny-custom.cfg","hand_detection/ai/yolo/v4-tiny.weights", ["hand"])
    
    def count_hands(self, image):
        _, _, results = self.model.inference(image)
        return len(results)