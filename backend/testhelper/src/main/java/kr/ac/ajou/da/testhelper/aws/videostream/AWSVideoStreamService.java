package kr.ac.ajou.da.testhelper.aws.videostream;

import com.amazonaws.services.kinesisvideo.AmazonKinesisVideo;
import com.amazonaws.services.kinesisvideo.AmazonKinesisVideoClient;
import com.amazonaws.services.kinesisvideo.model.CreateSignalingChannelRequest;
import com.amazonaws.services.kinesisvideo.model.CreateSignalingChannelResult;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class AWSVideoStreamService {
    private final AmazonKinesisVideo kinesisVideoClient;

    public AWSVideoStreamService() {
        this.kinesisVideoClient = AmazonKinesisVideoClient.builder().build();
    }

    public void createSignalingChannel(String channelName){
        CreateSignalingChannelRequest req = new CreateSignalingChannelRequest();
        req.setChannelName(channelName);
        req.setChannelType("SINGLE_MASTER");
        CreateSignalingChannelResult res = this.kinesisVideoClient.createSignalingChannel(req);
        log.info("Create Channel : {}", res.getChannelARN());
    }
}
