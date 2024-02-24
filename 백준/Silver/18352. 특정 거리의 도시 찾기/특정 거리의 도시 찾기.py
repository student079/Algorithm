import sys
import heapq

N, M, K ,X = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

# 다익스트라
res = [float('inf')] * (N+1)
res[X] = 0
q = []
heapq.heappush(q, (0,X))

while q:
    result_x, x = heapq.heappop(q)

    if result_x > res[x]:
        continue

    for i in graph[x]:
        cost = result_x + 1
        if res[i] > cost:
            res[i] = cost
            heapq.heappush(q, (res[i], i))

flag = 0
for i in range(1,N+1):
    if res[i] == K:
        flag += 1
        print(i)

if flag == 0:
    print(-1)