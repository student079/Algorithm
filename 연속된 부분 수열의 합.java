class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0,0};
        int left = 0;
        int right = 0;
        int sum = 0;
        int range = sequence.length + 1;

        // right를 증가시키며 sum
        for(right=0; right<sequence.length; right++) {
            sum += sequence[right];

            // sum이 k보다 크다면 left를 증가시켜서 범위 줄이기
            while(sum > k)
                sum -= sequence[left++];

            // 만약 k와 같다면 이전의 range와 비교 후 더 짧다면 업데이트
            if(sum == k) {
                if(range > right-left+1) {
                    range = right-left+1;
                    answer[0] = left;
                    answer[1] = right;
                }
                // 같다면 이전의 값과 비교하여 더 작은 값 선택
                else if(range == right-left+1) {
                    answer[0] = Math.min(answer[0], left);
                    answer[1] = Math.min(answer[1], right);
                }
            }

        }

        return answer;
    }
}