import sys
sys.setrecursionlimit(10**6)
# input
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

# undirected graph (don't know who is parent)
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# visiting check
visited = [0] * (N+1)

# DFS
def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2,N+1):
    print(visited[i])


