package kr.ac.ajou.da.testhelper.test.student;

import kr.ac.ajou.da.testhelper.definition.Device;
import kr.ac.ajou.da.testhelper.test.student.dto.RoomDto;
import kr.ac.ajou.da.testhelper.user.User;
import org.springframework.stereotype.Service;

@Service
public class TestStudentService {
    public RoomDto getRoom(Long testID, User student, Device device) {

        return new RoomDto(1L, device);
    }
}
