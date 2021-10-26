package kr.ac.ajou.da.testhelper.test.room;

import kr.ac.ajou.da.testhelper.definition.DeviceType;
import kr.ac.ajou.da.testhelper.submission.Submission;
import kr.ac.ajou.da.testhelper.submission.SubmissionService;
import kr.ac.ajou.da.testhelper.submission.exception.SubmissionNotFoundException;
import kr.ac.ajou.da.testhelper.test.room.dto.RoomDto;
import kr.ac.ajou.da.testhelper.test.room.dto.StudentRoomDto;
import kr.ac.ajou.da.testhelper.test.room.exception.RoomNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class TestRoomService {

    private final SubmissionService submissionService;

    @Transactional
    public RoomDto getRoom(Long testID, Long studentId, DeviceType deviceType) {

        Submission submission;

        try {
            submission = submissionService.getByTestIdAndStudentId(testID, studentId);
        } catch (SubmissionNotFoundException exception) {
            throw new RoomNotFoundException();
        }

        return new RoomDto(submission, deviceType);
    }

    public List<StudentRoomDto> createRoomsForStudents(Long testId, Long supevisedBy) {

        /**
         *  1. 시험 감독할 대학생 목록 조회
         *  2. 각 대학생을 위한 VideoStream Channel 생성
         *  3. 시험 감독 접속을 위한 정보 반환
         */

        List<Submission> submissions = submissionService.getByTestIdAndSupervisedBy(testId, supevisedBy);

        return submissions.stream()
                .map(StudentRoomDto::new)
                .collect(Collectors.toList());
    }
}
