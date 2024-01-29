# 다시 풀어보기

import sys
import bisect

#300000
# o(n^2) 는 안되고 nlogn으로
# 가장 긴 증가했다가 감소하는

N = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))

# 가장 긴 증가하는 수열을 
# 원래 꺼 하나 뒤집어서 하나
# 인덱스로 가장 긴 거 비교

rev_stones = stones[::-1]
inc_dp = [stones[0]]
dec_dp = [rev_stones[0]]
front = [1] * N
back = [1] * N

for i in range(N):
    if stones[i] > inc_dp[-1]:
        inc_dp.append(stones[i])
    else:
        idx = bisect.bisect_left(inc_dp, stones[i])
        inc_dp[idx] = stones[i]
    front[i] = len(inc_dp)
    
    if rev_stones[i] > dec_dp[-1]:
        dec_dp.append(rev_stones[i])
    else:
        idx = bisect.bisect_left(dec_dp, rev_stones[i])
        dec_dp[idx] = rev_stones[i]
    back[i] = len(dec_dp)

max_count = 0
for i in range(N):
    max_count = max(max_count, front[i] + back[N - i - 1] - 1)

print(max_count)
        
