import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, Integer> score = new HashMap<>();
        int pLength = photo.length;
        int[] answer = new int[pLength];

        for (int i = 0; i<yearning.length;i++)
            score.put(name[i],yearning[i]);

        for (int i = 0; i<pLength;i++) {
            int sum = 0;
            for (String yName : photo[i])
                sum += score.getOrDefault(yName, 0);
            answer[i] = sum;
        }
        return answer;
    }
}