import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK3052_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] hash = new int[42];
        for (int i = 0; i < 10; i++)
            hash[Integer.parseInt(br.readLine()) % 42]++;

        int sum = 0;
        for (int i : hash) {
            if (i != 0)
                sum++;
        }

        System.out.println(sum);

        br.close();
    }
}
