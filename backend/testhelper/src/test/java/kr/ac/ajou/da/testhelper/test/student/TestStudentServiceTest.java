package kr.ac.ajou.da.testhelper.test.student;

import kr.ac.ajou.da.testhelper.definition.Device;
import kr.ac.ajou.da.testhelper.submission.Submission;
import kr.ac.ajou.da.testhelper.submission.SubmissionService;
import kr.ac.ajou.da.testhelper.test.student.dto.RoomDto;
import kr.ac.ajou.da.testhelper.user.User;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


class TestStudentServiceTest {

    @InjectMocks
    private TestStudentService testStudentService;

    @Mock
    private SubmissionService submissionService;

    private User student = new User();

    @BeforeEach
    void init(){
        this.submissionService = mock(SubmissionService.class);
        this.testStudentService = new TestStudentService(submissionService);
    }

    @Test
    void getRoom_정상() {
        //given

        //testID와 student에 해당하는 SUBMISSION 가져오기
        when(submissionService.getByTestIDAndStudentID(anyLong(), anyLong())).thenReturn(new Submission(1L));

        //when
        RoomDto room = this.testStudentService.getRoom(1L, student, Device.PC);

        //then
        assertEquals(Device.PC, room.getDevice());
        assertEquals("1",room.getName());

    }
}