// 1 <= nums <= 10000
// set으로 중복 제거 후 개수
// 개수가 N/2보다 작거나 같으면 그대로
// 크면 N/2
import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int solution(int[] nums) {
        
        int N = nums.length;
        
        int count = Arrays.stream(nums)
            .boxed()
            .collect(Collectors.toSet())
            .size();
        
        if (count <= N/2) {
            return count;
        } else {
            return N/2;
        }
    }
}