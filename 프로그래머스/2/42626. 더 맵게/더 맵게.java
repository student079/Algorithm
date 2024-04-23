// 우선순위 큐로 가장 작은 수
// 백만

import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) {
            pq.add(s);
        }
        
        while (true) {
            if (pq.isEmpty())
                return -1;
            int a = pq.poll();
            if (a >= K) {
                return answer;
            }
            if (pq.isEmpty())
                return -1;
            int b = pq.poll();
            
            pq.add(a + (b*2));
            answer++;
        }
    }
}