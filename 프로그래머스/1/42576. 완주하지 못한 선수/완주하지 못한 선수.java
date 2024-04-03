// 1< = N <= 100000 십만
// 동명이인 있을 수 있음

import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        int completionLength = completion.length;
        
        for (int i = 0; i < completionLength; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }
        
        return participant[completionLength];
    }
}