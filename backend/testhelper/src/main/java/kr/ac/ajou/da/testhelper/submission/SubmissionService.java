package kr.ac.ajou.da.testhelper.submission;

import kr.ac.ajou.da.testhelper.submission.exception.SubmissionNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class SubmissionService {
    public Submission getByTestIDAndStudentID(Long testID, Long studentID) throws SubmissionNotFoundException {
        throw new SubmissionNotFoundException();
    }
}
