import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BAEK10818_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arrs = new int[N];

        for (int i = 0; i < N; i++)
            arrs[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arrs);

        System.out.printf("%d %d\n", arrs[0], arrs[N - 1]);

        br.close();
    }
}
