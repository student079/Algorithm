import sys

N = int(sys.stdin.readline())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
res = sys.maxsize

def dfs(L, idx):
    global res
    if L == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += table[i][j]
                elif not visited[i] and not visited[j]:
                    B += table[i][j]
        res = min(res, abs(A-B))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1,i+1)
            visited[i] = False

dfs(0,0)
print(res)
