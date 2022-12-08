from sys import stdin

T = int(stdin.readline().rstrip('\n'))
narr = []

for _ in range(T):
    narr.append(int(stdin.readline().rstrip('\n')))

narrMax = max(narr)

dp = [0, 1, 2, 4]

for i in range(4, narrMax+1):
    dp.append((dp[i-3]+dp[i-2]+dp[i-1]) % 1000000009)

for i in narr:
    print(dp[i])
