import sys

N,M = map(int,sys.stdin.readline().split())
sc = [0] * 101
for _ in range(N+M):
    a ,b = map(int,sys.stdin.readline().split())
    sc[a] = b

ans = 100
def dfs(visited,i,cnt):
    global ans

    if cnt >= ans:
        return

    if i >= 100:
        ans = min(ans,cnt)
        return

    for k in range(6,0,-1):

        if i + k > 100:
            continue

        if (visited[i+k] == -1) or (cnt < visited[i+k]):
            visited[i+k] = cnt
            if sc[i+k] != 0:
                dfs(visited,sc[i+k],cnt+1)
            else:
                dfs(visited,i+k,cnt+1)

visited = [-1] * 101
dfs(visited,1,0)
print(ans)