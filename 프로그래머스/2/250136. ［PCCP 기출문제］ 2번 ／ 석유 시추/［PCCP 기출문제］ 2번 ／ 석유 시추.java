// 가로 길이 500
// BFS 500 * 500 = 250000
// 해놓고 500 반복

import java.util.*;

class Solution {
    
    int[] dx = {1, 0, 0, -1};
    int[] dy = {0, 1, -1, 0};
    int n;
    int m;
    Map<Integer, Integer> info = new HashMap<>();
    
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[0].length;
        
        int idx = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1) {
                    bfs(idx, i, j, land);
                    idx++;
                }
            }
        }
        
        for (int i = 0; i < m; i++) {
            Set<Integer> st = new HashSet<>();
            int temp = 0;
            for (int j = 0; j < n; j++) {
                int index = land[j][i];
                if (index != 0 && !st.contains(index)) {
                    temp += info.get(index);
                    st.add(index);
                }
            }
            answer = Math.max(answer, temp);
        }
        
        
        return answer;
    }
    
    public void bfs(int idx, int i, int j, int[][] land) {
        Queue<int[]> q = new LinkedList<>();
        int count = 1;
        
        q.add(new int[] {i, j});
        land[i][j] = idx;
        
        while (!q.isEmpty()) {
            int[] xy = q.poll();
            
            for (int k = 0; k < 4; k++) {
                int nx = xy[0] + dx[k];
                int ny = xy[1] + dy[k];
                
                if (nx < n && nx >= 0 && ny < m && ny >= 0) {
                    if (land[nx][ny] == 1) {
                        land[nx][ny] = idx;
                        q.add(new int[] {nx,ny});
                        count++;
                    }
                }
            }
        }
        
        info.put(idx, count);
    }
}