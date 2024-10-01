import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int n = commands.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {
            int[] command = commands[i];
            
            int[] subArray = Arrays.copyOfRange(array,command[0]-1, command[1]);
            Arrays.sort(subArray);
            answer[i] = subArray[command[2]-1];
        }
        
        return answer;
    }
}