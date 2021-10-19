package kr.ac.ajou.da.testhelper.test.verification.dto;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
public class GetTestStudentVerificationResDto {
    private final Long testId;
    private final Long studentId;
    private final Long submissionId;

    private final Boolean verified;
}
