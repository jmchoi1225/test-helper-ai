from .rekognition import compare_faces

class IdCardValidationService:
    def __new__(cls): # singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(IdCardValidationService, cls).__new__(cls)
        return cls.instance
    
    def validate_id_card(self, test_id, student_number):
        idcard_path= self.__resolve_idcard_img_path(test_id, student_number)
        face_path = self.__resolve_face_img_path(test_id, student_number)

        return compare_faces(idcard_path, face_path)

    def __resolve_idcard_img_path(self, test_id, student_number):
        return "test/{test_id}/submission/{student_number}/student_card.jpg"

    def __resolve_face_img_path(self, test_id, student_number):
        return "test/{test_id}/submission/{student_number}/face.jpg"