//  길이 100

import java.util.Queue;
import java.util.PriorityQueue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        //         우선순위 큐로 최대값 가져오고
//         그거에 맞는 우선순위값 큐에서 가져오기
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < priorities.length ; i++) {
            pq.add(-priorities[i]);
            q.add(i);
        }
        
        while (!pq.isEmpty()) {
            int rank = pq.poll() * -1;
            
            while (priorities[q.peek()] != rank) {
                q.add(q.poll());
            }
            int index = q.poll();
            if (index == location) {
                break;
            }
            answer++;
            
        }

        return answer;
    }
}