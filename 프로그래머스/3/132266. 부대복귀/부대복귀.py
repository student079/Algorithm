# 	2878231000
# 다익스트라 뒤집어서
# log(500000* 500) 
# bfs
import heapq

def solution(n, roads, sources, destination):
    answer = []
    
    res = [float('inf')] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    
    q = []
    q.append((0, destination))
    res[destination] = 0
    
    while q:
        d, node = heapq.heappop(q)
        
        for to in graph[node]:
            if res[to] > d + 1:
                res[to] = d + 1
                heapq.heappush(q, (res[to], to))
    
    for i in sources:
        answer.append(res[i] if res[i] != float('inf') else -1)
    
    return answer