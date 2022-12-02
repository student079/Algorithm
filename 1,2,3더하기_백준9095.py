from sys import stdin

T = int(stdin.readline().rstrip('\n'))

dp = [0, 1, 2, 4]
n = []
for _ in range(T):
    n.append(int(stdin.readline().rstrip('\n')))

n_max = max(n)

for i in range(4, n_max + 1):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for i in n:
    print(dp[i])
