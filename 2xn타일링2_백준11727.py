# 점화식 구하기
import sys

n = int(sys.stdin.readline().rstrip('\n'))

dp = [0, 1, 3]

for i in range(3, n + 1):
    dp.append(dp[i - 1] + 2*dp[i - 2])

print(dp[n] % 10007)
