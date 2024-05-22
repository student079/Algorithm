class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        // 2차원 인접행렬
        int[][] graph = new int[n][n];
        
        // 이기면 1 지면 -1
        for (int[] result : results) {
            int a = result[0], b = result[1];
            graph[a-1][b-1] = 1;
            graph[b-1][a-1] = -1;
        }
        
        // 플로이드 와샬
        for (int k = 0; k < n; k ++) {
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j++) {
                    if (i == j || graph[i][j] != 0)
                        continue;
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1;
                        graph[j][k] = -1;
                        graph[k][i] = -1;
                        graph[j][i] = -1;
                    }
                }
            }
        }
        
        // 0이 하나인 애들은 확정
        for (int i = 0; i<n ;i++) {
            int cnt = 0;
            
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 0)
                    cnt += 1;
            }
            if (cnt == 1)
                answer++;
        }
        
        
        return answer;
    }
}