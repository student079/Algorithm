import sys

def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = True
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = False


N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
ans = sys.maxsize
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(ans)