
import java.util.*;
import java.io.*;

public class Main {
    static int N, K;
    static int[][] items, dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        items = new int[N][2];
        dp = new int[K+1][N+1];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            items[i][0] = w;
            items[i][1] = v;
        }

        for (int i = 1; i < K+1; i++) {
            for (int j = 1; j < N+1; j++) {
                int w = items[j-1][0];
                int v = items[j-1][1];

                if (i < w) {
                    dp[i][j] = dp[i][j-1];
                } else {
                    dp[i][j] = Math.max(dp[i-w][j-1] + v, dp[i][j-1]);
                }
            }
        }

        System.out.println(dp[K][N]);


    }
}
