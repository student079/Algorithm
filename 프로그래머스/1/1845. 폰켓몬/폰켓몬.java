// 1 <= nums <= 10000
// set으로 중복 제거 후 개수
// 개수가 N/2보다 작거나 같으면 그대로
// 크면 N/2
import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int solution(int[] nums) {
        
        return Arrays.stream(nums)
            .boxed()
            .collect(Collectors.collectingAndThen(
                Collectors.toSet(), set -> Integer.min(set.size(), nums.length / 2)
            ));
    }
}