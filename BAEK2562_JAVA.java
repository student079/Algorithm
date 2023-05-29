import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK2562_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int max = 0;
        int maxIdx = 0;
        for (int i = 0; i < 9; i++) {
            int temp = Integer.parseInt(br.readLine());
            if (max < temp) {
                max = temp;
                maxIdx = i;
            }
        }

        System.out.println(max);
        System.out.println(maxIdx + 1);

        br.close();
    }
}
