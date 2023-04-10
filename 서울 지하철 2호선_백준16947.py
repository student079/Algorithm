import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)

visited = []
cycle = set()
cy = False
def search_cycle(i,step,visited,start,temp):
    global cy
    for j in graph[i]:
        if j not in visited:
            visited.append(j)
            temp.append(j)
            search_cycle(j,step + 1,visited,start,temp)
            temp.remove(j)
            visited.remove(j)
        else:
            if step >= 3 and start in graph[i]:
                cy = True
                for k in temp:
                    cycle.add(k)
                return
visit = [-1] * (N+1)
def compute_distance():
    q = deque()
    
    for i in list(cycle):
        q.append(i)
        visit[i] = 0

    while q:
        x = q.popleft()

        for i in graph[x]:
            if visit[i] == -1:
                visit[i] = visit[x] + 1
                q.append(i)


for i in range(1,N+1):
    visited.append(i)
    search_cycle(i,1,visited,i,[i])
    if cy:
        break
    visited.remove(i)

compute_distance()
print(*visit[1:])