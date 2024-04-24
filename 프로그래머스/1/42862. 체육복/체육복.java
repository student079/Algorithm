//바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다
//최대한 많은 학생이 체육수업을 들어야 합니다.
// 우선순위를 앞사람 -> 뒷사람
//여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        // lost 배열 true : 잃어버림
        int[] lostList = new int[n+2];
        for (int l : lost) {
            lostList[l] = 1;
        }
        // reserve 배열 true : 여분 있음
        int[] reserveList = new int[n+2];
        for (int r : reserve) {
            reserveList[r] = 1;
            if (lostList[r] == 1) {
                lostList[r] = 0;
                reserveList[r] = 0;
            }
        }
        
        // 한명씩 돌면서 없으면 앞,뒤 순으로 찾기
        for (int i = 1; i <= n ; i++) {
            if (lostList[i] == 1) {
                if (reserveList[i-1] == 1) {
                    reserveList[i-1] = 0;
                    answer++;
                } else if (reserveList[i+1] == 1) {
                    reserveList[i+1] = 0;
                    answer++;
                }
            }
            else {
                answer++;
            }
        }
        
        return answer;
    }
}