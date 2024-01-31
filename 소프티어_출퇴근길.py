# 다시 풀어보기

import sys
sys.setrecursionlimit(1000000)

# n 100000
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
graphRev = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graphRev[b].append(a)
S, T = map(int,sys.stdin.readline().split())

def dfs(now, graph, visit):
        if visit[now]:
            return
        visit[now] = True
        for neighbor in graph[now]:
            dfs(neighbor, graph, visit)
        return

fromS = [False] * (n+1)
fromS[T] = True
dfs(S, graph, fromS)

toS = [False] * (n+1)
dfs(S, graphRev, toS)

fromT = [False] * (n+1)
fromT[S] = True
dfs(T, graph, fromT)

toT = [False] * (n+1)
dfs(T, graphRev, toT)

cnt = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1
print(cnt -2)