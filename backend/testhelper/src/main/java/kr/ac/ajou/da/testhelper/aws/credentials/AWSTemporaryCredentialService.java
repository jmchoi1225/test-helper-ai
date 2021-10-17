package kr.ac.ajou.da.testhelper.aws.credentials;

import com.amazonaws.services.securitytoken.AWSSecurityTokenService;
import com.amazonaws.services.securitytoken.AWSSecurityTokenServiceClientBuilder;
import com.amazonaws.services.securitytoken.model.Credentials;
import com.amazonaws.services.securitytoken.model.GetSessionTokenRequest;
import com.amazonaws.services.securitytoken.model.GetSessionTokenResult;
import org.springframework.stereotype.Service;

@Service
public class AWSTemporaryCredentialService {

    private static final int TEMPORARY_CREDENTIALS_DURATION = 900;
    private final AWSSecurityTokenService stsClient;

    public AWSTemporaryCredentialService() {
        this.stsClient = AWSSecurityTokenServiceClientBuilder.standard().build();
    }

    public Credentials createTemporaryCredential() {
        GetSessionTokenRequest req = new GetSessionTokenRequest();
        req.setDurationSeconds(TEMPORARY_CREDENTIALS_DURATION);
        GetSessionTokenResult res = stsClient.getSessionToken(req);
        return res.getCredentials();
    }


}
