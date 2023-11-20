import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] scores = new int[N];
        for (int i = 0; i < N; i++)
            scores[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(scores);
        double sum = 0;
        for (int i = 0; i < N; i++)
            sum += ((double) scores[i] / scores[N - 1]) * 100;
        sum /= N;

        System.out.println(sum);

        br.close();
    }
}
