import sys

N = int(sys.stdin.readline().rstrip('\n'))

dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, N+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else:
        dp[i] = 0
print(dp[N])

# https://jyeonnyang2.tistory.com/51 참고