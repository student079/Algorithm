import sys

N = int(sys.stdin.readline()) # N 100000

dp = [i for i in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        jj = j * j
        if jj > i:
            break

        if dp[i] > dp[i -jj] + 1:
            dp[i] = dp[i-jj] + 1

print(dp[N])


