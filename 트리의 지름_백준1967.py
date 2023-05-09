import sys
# n <= 10,000
sys.setrecursionlimit(10**5)

# input
n = int(sys.stdin.readline())
# DFS, graph
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(n-1):
    parent, child, distance = list(map(int,sys.stdin.readline().split()))
    graph[parent].append((child,distance))
    graph[child].append((parent,distance))

# DFS
def dfs(s,dis):
    for v,d in graph[s]:
        if visited[v] == -1:
            # distance store
            visited[v] = dis + d
            dfs(v,dis+d)

# search for most far node from 1 node
# so, assume that it is root
visited[1] = 0
dfs(1,0)
s = visited.index(max(visited))

# update distance from s
visited = [-1] * (n+1)
visited[s] = 0
dfs(s,0)
print(max(visited))