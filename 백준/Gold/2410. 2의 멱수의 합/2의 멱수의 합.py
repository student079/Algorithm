# N <= 1000000 백만

# dp
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0] * (N+1)

dp[1] = 1

# 홀수 -> N-1 에 1더한 것
# 짝수 -> N-1에 1 더한 것 + N/2에 2*곱해준것

for i in range(2, N+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] + dp[i//2]
    else:
        dp[i] = dp[i-1]

print(dp[N] % 1000000000)
