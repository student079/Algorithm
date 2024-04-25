// 숫자 20 개
// 2**20 백만
// dfs 가능

class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, 0, 0, target);
        
        return answer;
    }
    
    public void dfs(int[] numbers, int index, int value, int target) {
        if (index == numbers.length) {
            if (target == value) {
                answer++;
            }
            return;
        }
        
        dfs(numbers, index+1, value - numbers[index], target);
        dfs(numbers, index+1, value + numbers[index], target);
    }
}