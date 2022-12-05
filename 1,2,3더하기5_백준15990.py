from sys import stdin

T = int(stdin.readline().rstrip('\n'))
n = []
for _ in range(T):
    n.append(int(stdin.readline().rstrip('\n')))

n_max = max(n)
dp = [[0 for _ in range(4)] for _ in range(n_max+1)]
# [0, 1로끝나는 개수, 2로 끝나는 개수, 3으로 끝나는 개수]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, n_max + 1):
    dp[i] = [
        0,
        # -1힌깂은 +1 하면 i가 되는데 1이 연속으로 오면 안되니까
        (dp[i-1][2] + dp[i-1][3]) % 1000000009,
        # 똑같은 이유
        (dp[i-2][1] + dp[i-2][3]) % 1000000009,
        (dp[i-3][2] + dp[i-3][1]) % 1000000009,
    ]

for i in n:
    print(sum(dp[i]) % 1000000009)
