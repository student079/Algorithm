# 그래프 
# 거리
# 모든 노드의 최단 거리

# N 2 ~ 100, M 1 ~ 5000

import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    graph[a].append(b)
    graph[b].append(a)

# 다익스트라 N 번 돌리기?
# 시간상으로는 가능

def dijkstra(start) -> int:
    temp = [float('inf')] * (N+1)
    
    q = []
    temp[start] = 0
    q.append((0, start))

    while q:
        dis, node = heapq.heappop(q)

        if temp[node] < dis:
            continue
        
        for toNode in graph[node]:
            if temp[toNode] > dis + 1:
                temp[toNode] = dis + 1
                q.append((dis+1, toNode))

    return sum(temp[1:])


res = float('inf')
resIdx = -1

for i in range(1, N+1):
    temp = dijkstra(i)
    if temp < res:
        res = temp
        resIdx = i

print(resIdx)
