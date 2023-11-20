import java.util.*;
import java.io.*;

public class Solution {
    public Stack<Integer> solution(int []arr)  throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack = new Stack<>();

        for (int a: arr) {
            if (!stack.empty()) {
                if (!stack.peek().equals(a)) {
                    stack.push(a);
                }
            } else {
                stack.push(a);
            }
        }
        // while (!stack.empty()) {
        //     bufferedWriter.write(stack.pop());
        //     bufferedWriter.write("\n");
        //     bufferedWriter.flush();
        // }
        bufferedWriter.close();
        return stack;
    }
}