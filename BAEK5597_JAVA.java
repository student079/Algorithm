import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK5597_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] students = new int[31];

        for (int i = 0; i < 28; i++)
            students[Integer.parseInt(br.readLine())] = 1;

        for (int i = 1; i <= 30; i++) {
            if (students[i] == 0)
                System.out.println(i);
        }

        br.close();
    }
}
