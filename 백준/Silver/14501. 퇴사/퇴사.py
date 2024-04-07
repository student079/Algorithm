# N 1 ~ 15
# 2** 15 = 32768 완전 탐색 가능

import sys

N = int(sys.stdin.readline())
T = []
P = []
for _ in range(N):
    t, p = map(int,sys.stdin.readline().rstrip().split())
    T.append(t)
    P.append(p)

# dfs로 할지 안할지
# 안되는 건 걍 안되고
answer = 0

def dfs(idx, delay, money):
    global answer

    if idx >= N:
        answer = max(answer, money)
        return

    if delay > 0:
        dfs(idx + 1, delay - 1, money)
    elif idx + T[idx] > N:
        dfs(idx+1, delay, money)
    else:
        dfs(idx+1, T[idx] - 1, money + P[idx])
        dfs(idx + 1, delay, money)

dfs(0, 0, 0)

print(answer)