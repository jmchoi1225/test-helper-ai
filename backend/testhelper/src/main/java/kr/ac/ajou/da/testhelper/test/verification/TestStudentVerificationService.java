package kr.ac.ajou.da.testhelper.test.verification;

import kr.ac.ajou.da.testhelper.test.verification.dto.GetTestStudentVerificationResDto;
import org.springframework.stereotype.Service;

import java.util.LinkedList;
import java.util.List;

@Service
public class TestStudentVerificationService {

    public List<GetTestStudentVerificationResDto> getList(Long testId, Long proctorId) {

        LinkedList<GetTestStudentVerificationResDto> resDto = new LinkedList<>();

        resDto.add(new GetTestStudentVerificationResDto(testId,1L,1L,true));

        return resDto;

    }

    public boolean update(Long testId, Long studentId, Boolean verified) {

        return true;
    }
}
