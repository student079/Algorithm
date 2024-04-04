import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        int N = progresses.length;
        Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < N ; i++) {
            q.add((int)Math.ceil((100.0- progresses[i]) / speeds[i]));
        }
        
        int s = 1;
        int day = q.poll();
        while (!q.isEmpty()) {
            if (day >= q.peek()) {
                s++;
                q.poll();
            } else {
                answer.add(s);
                s = 1;
                day = q.poll();
            }
        }
        answer.add(s);
        
        return answer;
    }
}