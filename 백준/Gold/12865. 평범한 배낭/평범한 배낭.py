import sys

N, K = map(int ,sys.stdin.readline().rstrip().split())
items = []
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        w, v = items[j-1]

        if i < w:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i - w][j-1] + v, dp[i][j-1])

print(dp[K][N])