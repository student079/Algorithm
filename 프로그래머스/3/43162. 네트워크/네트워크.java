class Solution {
    int answer = 0;
    
    public int solution(int n, int[][] computers) {
        // 방문기록
        int[] visited = new int[n];
        
        for (int i = 0; i < n; i++)
            if (visited[i] == 0) {
                dfs(i, computers, visited, n);
                answer++;
            }
        
        return answer;
    }
    
    public void dfs(int node, int[][] computers, int[] visited, int n) {
        if (visited[node] == 0) {
            visited[node] = 1;
            for (int i = 0; i < n; i++) {
                if (i != node && computers[node][i] == 1)
                    dfs(i, computers, visited, n);
            }
        }
    }
}