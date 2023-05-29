import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK27866_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().trim();
        int i = Integer.parseInt(br.readLine());
        System.out.println(str.charAt(i - 1));

        br.close();

    }
}
