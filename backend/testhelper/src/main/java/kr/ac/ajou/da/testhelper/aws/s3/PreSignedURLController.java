package kr.ac.ajou.da.testhelper.aws.s3;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.amazonaws.HttpMethod;

@RestController
public class PreSignedURLController {
	@Autowired
	private PreSignedURLService preSignedURLService;
	
	private static final long expiration_time = 1000 * 60 * 3; // 3분;
	private static final String bucket_name = "testhelper";

	@GetMapping(path="/s3-upload-url")
	public String GetS3UrlUpload(@RequestParam String objectKey) {
		return preSignedURLService.getPreSignedURL(objectKey, expiration_time, bucket_name, HttpMethod.PUT);
	}
	
	@GetMapping(path="/s3-download-url")
	public String GetS3UrlDownload(@RequestParam String objectKey)  throws IOException {
		return preSignedURLService.getPreSignedURL(objectKey, expiration_time, bucket_name, HttpMethod.GET);
	}
}
