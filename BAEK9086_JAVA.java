import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK9086_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String str = br.readLine().trim();
            System.out.printf("%c%c\n", str.charAt(0), str.charAt(str.length() - 1));
        }

        br.close();

    }
}
