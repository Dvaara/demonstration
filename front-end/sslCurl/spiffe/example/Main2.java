//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package spiffe.example;

import java.io.IOException;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.conn.ssl.NoopHostnameVerifier;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class Main {
    public Main() {
    }

    public static void main(String... args) {
        String url = args[0];
        CloseableHttpClient httpClient = HttpClients.custom().useSystemProperties().setSSLHostnameVerifier(new NoopHostnameVerifier()).build();
        HttpGet get = new HttpGet(url);
        String response = makeCall(httpClient, get);
        System.out.println(response);
        System.exit(1);
    }

    private static String makeCall(CloseableHttpClient httpClient, HttpGet get) {
        try {
            CloseableHttpResponse response = httpClient.execute(get);
            HttpEntity entity = response.getEntity();
            return EntityUtils.toString(entity);
        } catch (IOException var4) {
            var4.printStackTrace();
            return null;
        }
    }
}
