import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK10813_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] buckets = new int[N + 1];
        for (int i = 0; i <= N; i++)
            buckets[i] = i;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int temp = buckets[a];
            buckets[a] = buckets[b];
            buckets[b] = temp;
        }

        for (int i = 1; i <= N; i++)
            System.out.printf("%d ", buckets[i]);

        System.out.println();

        br.close();
    }
}
