import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BAEK10809_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().trim();
        int[] alpha = new int[26];

        char c = 'a';
        for (int i = 0; i < 26; i++) {
            alpha[i] = str.indexOf(c);
            c++;
        }

        for (int i = 0; i < 26; i++)
            System.out.printf("%d ", alpha[i]);
        System.out.println();

        br.close();
    }
}
