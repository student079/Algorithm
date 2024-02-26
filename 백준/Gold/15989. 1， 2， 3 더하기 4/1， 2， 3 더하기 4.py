# n <= 10000
import sys

T = int(sys.stdin.readline())

ns = []
for _ in range(T):
    ns.append(int(sys.stdin.readline()))

n = max(ns)
dp = [1] * (n+1)
dp[1] = 1 # 1

# 2가 추가되는 경우
for i in range(2, n+1):
    dp[i] += dp[i - 2]

# 3이 추가되는 경우
for i in range(3, n+1):
    dp[i] += dp[i - 3]

for i in ns:
    print(dp[i])