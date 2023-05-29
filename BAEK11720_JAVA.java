import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK11720_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String str = br.readLine().trim();
        char[] strArr = str.toCharArray();

        int sum = 0;
        for (int i = 0; i < strArr.length; i++)
            sum += (int) strArr[i] - 48;

        System.out.println(sum);

        br.close();
    }
}
