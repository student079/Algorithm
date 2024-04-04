// 1 ~ 1000000 백만

import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        Arrays.sort(phone_book);
        
        for (int i = 0; i < phone_book.length - 1 ; i++) {
            String first = phone_book[i];
            String second = phone_book[i+1];
            if (first.length() <= second.length()) {
                if (first.equals(second.substring(0, first.length()))) {
                    answer = false;
                    break;
                }
            }
        }
        
        return answer;
    }
}