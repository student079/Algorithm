from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    
    dis = [0] * (n+1)
    dis[1] = 1
    def bfs(start):
        q = deque()
        q.append(start)
        while q:
            i = q.popleft()
            for j in graph[i]:
                if dis[j] == 0:
                    dis[j] = dis[i] + 1
                    q.append(j)
    bfs(1)
    m = 0
    res = 1
    for i in dis:
        if i > m:
            res = 1
            m = i
        elif i == m:
            res += 1
    
    return res