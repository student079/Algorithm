// truck_weights의 길이는 1 이상 10,000 이하
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        Queue<Integer> bridge = new LinkedList<>();
        Queue<Integer> truck = new LinkedList<>();
        int curWeight = 0;
        int curLength = 0;
        int count = 0;
        int N = truck_weights.length;
        while (count < N) {
            // 다리에서 나가는 트럭
            if (!bridge.isEmpty() && bridge.peek() + bridge_length == time) {
                bridge.poll();
                int w = truck.poll();
                curWeight -= w;
                curLength -= 1;
            }
            
            int w = truck_weights[count];
            if (curWeight + w <= weight && curLength + 1 <= bridge_length) {
                curWeight += w;
                curLength += 1;
                bridge.add(time);
                truck.add(w);
                count++;
            }
            time++;
        }
        
        return time + bridge_length;
    }
}