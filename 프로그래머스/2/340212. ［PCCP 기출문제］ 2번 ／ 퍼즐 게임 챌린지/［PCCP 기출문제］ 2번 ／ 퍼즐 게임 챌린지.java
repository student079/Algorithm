// 딱봐도 이분탐색인데용
// 30만문제
// 난이도 최대 10만

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1, right = 100000;
        int n = diffs.length;
        
        while (left <= right) {
            int level = (left + right) / 2;
            
            long totalTime = 0;
            int time_prev = 0;
            for (int i = 0; i < n; i++) {
                int diff = diffs[i];
                int time_cur = times[i];
                
                if (diff <= level) {
                    time_prev = time_cur;
                    totalTime += time_cur;
                } else {
                    int count = diff - level;
                    totalTime += count * (time_cur + time_prev) + time_cur;
                    time_prev = time_cur;
                }
            }
            
            if (totalTime <= limit) {
                right = level - 1;
            } else {
                left = level + 1;
            }
            
        }
        return left;
    }
}