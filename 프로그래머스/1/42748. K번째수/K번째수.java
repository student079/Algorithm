import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        int idx = 0;
        for (int[] command : commands) {
            int i = command[0], j = command[1], k = command[2];
            ArrayList<Integer> list = new ArrayList<>();
            for (int t = i-1; t < j ; t++ ) {
                list.add(array[t]);
            }
            list.sort((o1, o2) -> o1-o2);
            answer[idx++] = list.get(k-1);
        } 
        
        return answer;
    }
}