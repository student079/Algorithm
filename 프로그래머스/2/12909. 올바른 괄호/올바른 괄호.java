import java.util.Stack;

class Solution {
    boolean solution(String s) {
        
        Stack<String> stack = new Stack<>();
        
        for (int i = 0; i < s.length() ; i++) {
            String c = String.valueOf(s.charAt(i));
            
            if (c.equals("(")) {
                stack.push(c);
            } else {
                if ( !stack.isEmpty()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        
        if (stack.isEmpty()) return true;
        else return false;
    }
}