import java.util.*;

class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;

        for (int i=1; i<=r2; i++) {
            // 작은 원 x=i 일때 y값에 올림
            long small = (int) Math.ceil(Math.sqrt(1.0*r1*r1 - 1.0*i*i));
            // 큰 원 x=i 일때 y값에 내림
            long big = (int) Math.floor(Math.sqrt(1.0*r2*r2 - 1.0*i*i));

            // +1해줘야 갯수가 맞는데 왜그런지 모르겠네
            answer += (big - small + 1);

        }

        return answer * 4;
    }
}