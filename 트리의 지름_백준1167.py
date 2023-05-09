import sys

# input
V = int(sys.stdin.readline())
# DFS, graph
graph = [[] for _ in range(V+1)]
visited = [-1] * (V+1)

for _ in range(V):
    # detach last -1
    com = list(map(int,sys.stdin.readline().split()))[:-1]
    vertex = com.pop(0)
    # make graph
    # (vertex, distance)
    while com:
        graph[vertex].append((com.pop(0),com.pop(0)))

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
visited = [-1] * (V+1)
visited[s] = 0
dfs(s,0)
print(max(visited))