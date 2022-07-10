from .rekognition import detect_text

class StudentNumberValidationService:
    def __new__(cls): # singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(StudentNumberValidationService, cls).__new__(cls)
        return cls.instance

    def validate_student_number(self, test_id, student_number):
        idcard_path= self.__resolve_idcard_img_path(test_id, student_number)

        idcards_texts = detect_text(idcard_path)

        return student_number in idcards_texts

    def __resolve_idcard_img_path(self, test_id, student_number):
        return "test/{test_id}/submission/{student_number}/student_card.jpg"
