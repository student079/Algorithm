import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        ArrayList<String> nums = new ArrayList<String>();
        
        // 문자열로 받아서
        for (int num : numbers) {
            nums.add(String.valueOf(num));
        }
        
        // 정렬
        nums.sort((o1, o2) -> ((o2+o1).compareTo(o1+o2)));
        
        if (nums.get(0).equals("0")) {
            return "0";
        }
        
        return String.join("", nums);
    }
}