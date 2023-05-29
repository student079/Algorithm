import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK11654_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().trim();

        System.out.println((int) str.charAt(0));
        br.close();

    }
}
