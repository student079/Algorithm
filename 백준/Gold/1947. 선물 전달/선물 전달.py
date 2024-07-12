# N 1~1000000

import sys

N = int(sys.stdin.readline())
if N == 1:
    print(0)
else:
    dp = [0] * (N+1)

    dp[1], dp[2] = 0,1
    for i in range(3, N+1):
        dp[i] = ((dp[i-1] + dp[i-2]) * (i-1)) % 1000000000

    print(dp[N])