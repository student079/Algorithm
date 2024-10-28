// N 100,000
// M 100,000

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M; // 500
    static int[][] board, dp;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        board = new int[M][N];
        dp = new int[M][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        dfs(0, 0);
        System.out.println(dp[0][0]);

    }

    public static int dfs(int i, int j) {
        if (i == M - 1 && j == N - 1) {
            return 1;
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        dp[i][j] = 0;
        for (int k = 0; k < 4; k++) {
            int newI = i + dx[k], newJ = j + dy[k];

            if (!(newI >= 0 && newI < M && newJ >= 0 && newJ < N))
                continue;

            if (board[newI][newJ] < board[i][j]) {
                dp[i][j] += dfs(newI, newJ);
            }
        }

        return dp[i][j];
    }
}
