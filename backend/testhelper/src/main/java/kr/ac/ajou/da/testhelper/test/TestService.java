package kr.ac.ajou.da.testhelper.test;

import kr.ac.ajou.da.testhelper.course.Course;
import kr.ac.ajou.da.testhelper.test.definition.TestType;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class TestService {

    public Test getTest(Long testID) {

        return new Test(testID, TestType.MID, LocalDateTime.now(), LocalDateTime.now(), new Course(1L, "name"));
    }
}
