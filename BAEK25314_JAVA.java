import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK25314_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String str = "";
        for (int i = 0; i<(N/4);i++) {
            str += "long ";
        }
        str += "int";

        System.out.println(str);

        br.close();
    }
}
