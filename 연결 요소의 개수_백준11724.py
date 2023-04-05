import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a ,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
visited[0] = True

def bfs(start, visited):
    q = deque()

    q.append(start)
    while q:
        temp = q.popleft()

        for i in graph[temp]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

            


component = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i,visited)
        component += 1

print(component)