// 최단 거리, BFS

import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<int[]> q = new LinkedList<>();
        int[] dx = new int [] {1, 0, -1, 0};
        int[] dy = new int [] {0, -1, 0, 1};
        int[][] visited = new int[n][m];
        visited[0][0] = 1;
        q.add(new int[] {0,0});
        
        while (!q.isEmpty()) {
            int[] pos = q.poll();
            int x = pos[0];
            int y = pos[1];
            
            if (x == n-1 && y == m-1) {
                return visited[x][y];
            }
            
            for (int i = 0; i < 4; i ++ ){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                
                if (maps[nx][ny] == 0)
                    continue;
                
                if (visited[nx][ny] == 0 || visited[nx][ny] > visited[x][y] + 1) {
                    visited[nx][ny] = visited[x][y] + 1;
                    q.add(new int[] {nx,ny});
                }
            }
        }
        
        return -1;
    }
}