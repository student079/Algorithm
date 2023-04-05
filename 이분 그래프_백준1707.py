import sys
from collections import deque

K = int(sys.stdin.readline())

ans = True

def bfs(start):
    global ans

    q = deque()

    q.append(start)
    visited[start] = 1
    while q:
        temp = q.popleft()

        for i in graph[temp]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = -1 * visited[temp]
            elif visited[i] == visited[temp]:
                ans = False
                return


for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    visited[0] = 0

    for _ in range(E):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if visited[i] == 0:
            bfs(i)
            if not ans:
                print("NO")
                ans = True
                break
    else:
        print("YES")
    



