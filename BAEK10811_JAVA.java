import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BAEK10811_JAVA {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] buckets = new int[N + 1];
        for (int i = 1; i <= N; i++)
            buckets[i] = i;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            while (start < end) {
                int temp = buckets[start];
                buckets[start] = buckets[end];
                buckets[end] = temp;
                start++;
                end--;
            }
        }

        for (int i = 1; i <= N; i++)
            System.out.printf("%d ", buckets[i]);

        System.out.println();

        br.close();
    }
}
