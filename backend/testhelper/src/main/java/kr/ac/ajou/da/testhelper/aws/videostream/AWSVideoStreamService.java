package kr.ac.ajou.da.testhelper.aws.videostream;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.kinesisvideo.AmazonKinesisVideo;
import com.amazonaws.services.kinesisvideo.AmazonKinesisVideoClient;
import com.amazonaws.services.kinesisvideo.model.*;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class AWSVideoStreamService {
    private final AmazonKinesisVideo kinesisVideoClient;

    public AWSVideoStreamService() {
        this.kinesisVideoClient = AmazonKinesisVideoClient.builder()
                .withRegion(Regions.US_EAST_2)
                .build();
    }

    public void createSignalingChannel(String channelName) {
        try{
            describeSignalingChannel(channelName);
            log.info("{} channel exists", channelName);
            return;
        }catch (ResourceNotFoundException ignore){}

        CreateSignalingChannelRequest req = new CreateSignalingChannelRequest();
        req.setChannelName(channelName);
        req.setChannelType("SINGLE_MASTER");
        CreateSignalingChannelResult res = this.kinesisVideoClient.createSignalingChannel(req);
        log.info("Create Channel : {} {}", channelName, res.getChannelARN());
    }

    public void deleteSignalingChannel(String channelName) {
        try {
            ChannelInfo channelInfo = describeSignalingChannel(channelName);

            DeleteSignalingChannelRequest req = new DeleteSignalingChannelRequest();
            req.setChannelARN(channelInfo.getChannelARN());
            req.setCurrentVersion(channelInfo.getVersion());
            DeleteSignalingChannelResult res = this.kinesisVideoClient.deleteSignalingChannel(req);

            log.info("Deleted Channel : {} {}", channelName, channelInfo.getChannelARN());

        } catch (Exception ignored) {
            log.info("{} channel doesn't exist", channelName);
        }
    }

    private ChannelInfo describeSignalingChannel(String channelName) throws ResourceNotFoundException {
        DescribeSignalingChannelRequest req = new DescribeSignalingChannelRequest();
        req.setChannelName(channelName);
        return this.kinesisVideoClient.describeSignalingChannel(req).getChannelInfo();
    }
}
