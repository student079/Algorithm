// 1 이상 1,000,000 이하인 문자열 배열
// 우선순위큐 두개
// count로 전체 개수 관리

import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int count = 0;
        PriorityQueue<Integer> minPq = new PriorityQueue<>();
        PriorityQueue<Integer> maxPq = new PriorityQueue<>((o1, o2) -> o2-o1);
        
        for (String operation : operations) {
            String[] command = operation.split(" ");
            
            if (command[0].equals("I")) {
                minPq.add(Integer.parseInt(command[1]));
                maxPq.add(Integer.parseInt(command[1]));
                count++;
            }
            else {
                if (command[1].equals("1") && count > 0) {
                    int temp = maxPq.poll();
                    minPq.remove(temp);
                    count--;
                }
                else if (command[1].equals("-1") && count > 0) {
                    int temp = minPq.poll();
                    maxPq.remove(temp);
                    count--;
                }
            }
        }
        
        if (count > 0) {
            return new int[] {maxPq.poll(), minPq.poll()};
        } else {
            return new int[] {0, 0};
        }
    }
}