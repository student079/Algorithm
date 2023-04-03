#pypy3

import sys

N, M = map(int,sys.stdin.readline().split())

graph = [[] * N for i in range(N)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer = False
visited = [False] * 2001
def dfs(idx, depth):
    global answer
    visited[idx] = True

    if depth == 4:
        answer = True
        return

    for i in graph[idx]:
        if not visited[i]:
            dfs(i,depth+1)
            visited[i] = False
        

for i in range(N):
    dfs(i,0)
    visited[i] = False

if answer:
    print("1")
else:
    print("0")