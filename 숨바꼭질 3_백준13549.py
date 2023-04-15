import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
visited = [-1] * 100001
def bfs():
    q = deque()
    q.append(N)
    visited[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        i = 2*x
        if 0<= i <= 100000 and (visited[i] > visited[x] or visited[i] == -1):
            visited[i] = visited[x]
            q.append(i) 
        for i in [x+1,x-1]:
            if 0<= i <= 100000 and (visited[i] == -1 or visited[i] > visited[x]):
                visited[i] = visited[x] + 1
                q.append(i)
        
bfs()