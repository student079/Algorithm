// 소요시간 작은 순서
// 소수점 이하의 수는 버립니다

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int count = 0;
        int end = 0;
        int jobLength = jobs.length;
        
        // jobs 요청순으로 정렬
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        
        // 시간별로 요청처리
        int jobIdx = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        while (count < jobLength) {
            while (jobIdx < jobLength && jobs[jobIdx][0] <= end) {
                pq.add(jobs[jobIdx++]);
            }
            
            if (!pq.isEmpty()) {
                int[] temp = pq.poll();
                answer += temp[1] + end - temp[0];
                end += temp[1];
                count++;
            }
            else {
                end = jobs[jobIdx][0];
            }
        }
        
        return (int) Math.floor(answer / jobLength);
    }
}