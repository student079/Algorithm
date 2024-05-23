import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // N 200
        // bfs O(40000 * 6)
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine());
        String[] ts = bufferedReader.readLine().split(" ");
        int r1 = Integer.parseInt(ts[0]), c1 = Integer.parseInt(ts[1]);
        int r2 = Integer.parseInt(ts[2]), c2 = Integer.parseInt(ts[3]);

        int[] dx = {-2, -2, 0, 0, 2, 2};
        int[] dy = {-1, 1, -2, 2, -1, 1};

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(r1, c1, 0));
        boolean[][] visited = new boolean[N+1][N+1];
        visited[r1][c1] = true;

        while(!q.isEmpty()) {
            Node node = q.poll();

            if (node.x == r2 && node.y == c2) {
                System.out.println(node.cnt);
                System.exit(0);
            }

            for (int k = 0; k < 6; k ++) {
                int nx = node.x + dx[k];
                int ny = node.y + dy[k];

                if (!(0 <= nx && nx < N+1 && 0 <= ny && ny < N+1))
                    continue;

                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.add(new Node(nx, ny, node.cnt + 1));
                }
            }
        }
        System.out.println(-1);
    }

    public static class Node {
        int x, y, cnt;

        Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
