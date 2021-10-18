package kr.ac.ajou.da.testhelper.test.student.dto;

import kr.ac.ajou.da.testhelper.definition.Device;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor(access = AccessLevel.PRIVATE)
@Getter
public class RoomDto {
    //channelName
    private final String name;
    //clientID
    private final Device device;

    public RoomDto(Long submissionID, Device device) {
        this.name = submissionID.toString();
        this.device = device;
    }
}
