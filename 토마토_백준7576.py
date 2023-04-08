import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
tomato = {}
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        tomato[(i, j)] = row[j]

def bfs():

    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    while q:
        x,y =q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

           
            if (nx, ny) in tomato and tomato[(nx, ny)] == 0:
                tomato[(nx,ny)] = tomato[(x,y)]+1
                q.append((nx,ny))


q = deque()
for i in range(N):
    for j in range(M):
        if (i, j) in tomato and tomato[(i, j)] == 1:
            q.append((i,j))

bfs()

res = 0
for val in tomato.values():
    if val == 0:
        print("-1")
        exit()
    res = max(res, val)

print(res-1)