// 10000 완탐가능
// 가로세로중 큰값 작은값

import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int s = 0, b = 0;
        
        for (int[] size : sizes) {
            Arrays.sort(size);
            int big = size[1], small = size[0];
            
            if (b < big) {
                b = big;
            }
            
            if (s < small) {
                s = small;
            }
        }
        
        return b*s;
    }
}