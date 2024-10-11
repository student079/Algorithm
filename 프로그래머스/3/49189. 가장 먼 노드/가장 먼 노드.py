# 다익스트라
# 50000 * log 20000

import heapq

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    d = [float("inf")] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = []
    d[1] = 0
    heapq.heappush(q, (0, 1))
    
    while q:
        distance, node = heapq.heappop(q)
        if distance > d[node]:
            continue
            
        for next in graph[node]:
            if d[next] > distance + 1:
                d[next] = distance + 1
                heapq.heappush(q, (distance + 1, next))
    
    maxD = max(d[1:])
    for r in d:
        if r == maxD:
            answer+=1
    
    return answer