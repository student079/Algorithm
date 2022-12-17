from sys import stdin
INF = 10**6 + 1
R, G, B = 0, 1, 2

N = int(stdin.readline().rstrip('\n'))
home = [[-1, -1, -1]]
for _ in range(N):
    home.append(list(map(int, stdin.readline().rstrip('\n').split())))

# 첫시작을 고정해버리기
answer = INF
for color in [R, G, B]:
    dp = [[-1]*3 for _ in range(N+1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = home[1][color]

    for i in range(2, N+1):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + home[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + home[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + home[i][B]
# 마지막을 처음꺼랑 다르게 하려고 INF주기
    dp[N][color] = INF
    answer = min(answer, min(dp[N]))

print(answer)
