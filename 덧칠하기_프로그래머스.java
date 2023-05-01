class Solution {
    public int solution(int n, int m, int[] section) {
        int pre = 0;
        int res = 0;

        for (int idx = 0; idx<section.length ;idx++) {
            if (section[idx] >= pre){
                res++;
                pre = section[idx] + m;
            }
        }

        return res;
    }
}