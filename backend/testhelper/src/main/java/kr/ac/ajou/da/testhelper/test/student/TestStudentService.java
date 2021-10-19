package kr.ac.ajou.da.testhelper.test.student;

import kr.ac.ajou.da.testhelper.definition.Device;
import kr.ac.ajou.da.testhelper.submission.Submission;
import kr.ac.ajou.da.testhelper.submission.SubmissionService;
import kr.ac.ajou.da.testhelper.submission.exception.SubmissionNotFoundException;
import kr.ac.ajou.da.testhelper.test.student.dto.RoomDto;
import kr.ac.ajou.da.testhelper.test.student.exception.RoomNotFoundException;
import kr.ac.ajou.da.testhelper.student.Student;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class TestStudentService {

    private final SubmissionService submissionService;

    public RoomDto getRoom(Long testID, Student student, Device device) {

        Submission submission;

        try{
            submission = submissionService.getByTestIDAndStudentID(testID, student.getId());
        }catch(SubmissionNotFoundException exception){
            throw new RoomNotFoundException();
        }

        return new RoomDto(submission.getId(), device);
    }
}
