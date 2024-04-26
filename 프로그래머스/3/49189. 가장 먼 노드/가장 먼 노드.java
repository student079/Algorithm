// 1번 노드에서 가장 멀리 떨어진 노드의 갯수
// 다익스트라
// 최대값 몇개인지
// n 2 ~ 20000
// m 1 ~ 50000
// 다익스트라 45만

import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for (int i = 0; i <= n ; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        for (int[] e : edge) {
            int a = e[0], b = e[1];
            graph[a].add(b);
            graph[b].add(a);
        }
        
        int[] res = new int[n+1];
        Arrays.fill(res, Integer.MAX_VALUE);
        res[1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]); 
        pq.add(new int[]{0, 1});
        while (!pq.isEmpty()) {
            int[] q = pq.poll();
            int dis = q[0], node = q[1];
            
            if (dis < res[node]) continue;
            
            for (int i = 0; i < graph[node].size(); i++){
                if (res[graph[node].get(i)] > dis + 1) {
                    res[graph[node].get(i)] = dis+1;
                    pq.add(new int[]{dis+1, graph[node].get(i)});
                }
            }
            
        }
        
        // 최대값 구하기
        int max = 0;
        for (int i = 1; i < n+1 ; i++ ){
            if (max < res[i])
                max = res[i];
        }
        
        // 최대값 개수 세기
        for (int i = 1; i < n+1 ; i++ ){
            if (res[i] == max){
                answer++;
            }
        }
        
        return answer;
    }
}