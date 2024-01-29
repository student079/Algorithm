# 다시 풀어보기
# 이분 탐색 방법은 NlogN

import sys
import bisect

N = int(sys.stdin.readline())
heights = list(map(int,sys.stdin.readline().split()))

# 3000개
# 증가하는 최대 길이
# DP


# dp = [1] * N

# for i in range(N):
#     for j in range(i):
#         if heights[i] > heights[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))

# 이분탐색 방법도 있다

dp = [heights[0]]

for i in range(N):
    if heights[i] > dp[-1]:
        dp.append(heights[i])
    else:
        idx = bisect.bisect_left(dp,heights[i])
        dp[idx] = heights[i]

print(len(dp))
