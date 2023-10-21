import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e,w))

def dijkstra(start):
    res = [float('inf')] * (N+1)
    res[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        result_x, x = heapq.heappop(q)

        if res[x] < result_x:
            continue

        for d, w in graph[x]:
            if res[d] > result_x + w:
                res[d] = result_x + w
                heapq.heappush(q, (res[d],d))
    return res

s, e = map(int,sys.stdin.readline().split())

print(dijkstra(s)[e])