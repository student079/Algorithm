# dfs, bfs
from collections import deque
from collections import defaultdict

def solution(n, path, order):
    
    visited = [0] * n
    graph = [[] for _ in range(n)]
    orders = defaultdict(int)
    for a, b in order:
        orders[b] = a
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    visited[0] = 1
    q.append(0)
    after = dict()
    
    while q:
        node = q.popleft()
        
        if visited[orders[node]] != 1:
            after[orders[node]] = node
            continue
        
        visited[node] = 1
        
        for room in graph[node]:
            if visited[room] == 0:
                q.append(room)
        
        if node in after.keys():
            q.append(after[node])
        
    if sum(visited) == n:
        return True
    
    return False