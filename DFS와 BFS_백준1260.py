import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())
graph = [[False] * (N+1) for i in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(start,visited):
    if len(visited) == N:
        return

    visited.append(start)
    for i in range(1,N+1):
        if graph[start][i] and i not in visited:
            dfs(i,visited)



def bfs(start,visited):

    q = deque()

    q.append(start)
    while q:
        s = q.popleft()
        visited.append(s)

        for i in range(1,N+1):
            if graph[s][i] and i not in visited and i not in q:
                q.append(i)
        
    return
    

v = []
dfs(V,v)
print(*v)
v = []
bfs(V,v)
print(*v)