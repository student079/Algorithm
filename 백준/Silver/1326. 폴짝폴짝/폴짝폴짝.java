import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // bfs 10000 * 10000
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine());
        String[] ts = bufferedReader.readLine().split(" ");
        int[] bridge = new int[N];
        for (int i = 0; i < N; i++)
            bridge[i] = Integer.parseInt(ts[i]);
        String[] ts2 = bufferedReader.readLine().split(" ");
        int a = Integer.parseInt(ts2[0]), b = Integer.parseInt(ts2[1]);
        int[] visited = new int[N];
        visited[a - 1] = 1;

        Queue<Integer> q = new LinkedList<>();
        q.add(a-1);

        while(!q.isEmpty()) {
            int idx = q.poll();

            if (idx == b-1) {
                System.out.println(visited[idx]-1);
                System.exit(0);
            }

            for (int i = 0; i < N; i++) {
                if (visited[i] != 0)
                    continue;

                if ((i - idx) % bridge[idx] == 0) {
                    q.add(i);
                    visited[i] = visited[idx] + 1;
                }
            }
        }

        System.out.println(-1);
    }

}
