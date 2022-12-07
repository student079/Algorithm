from sys import stdin

N = int(stdin.readline().rstrip('\n'))
seq = list(map(int, stdin.readline().rstrip('\n').split()))

INF = -float("inf")
dp = [INF] * 100002
dp[0] = seq[0]

for i in range(1, N):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + seq[i]
    else:
        dp[i] = seq[i]

print(max(dp))
