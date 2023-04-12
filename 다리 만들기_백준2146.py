import sys
from collections import deque

N = int(sys.stdin.readline())

maps = []
for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))
visited = [[False] * N for _ in range(N)]

count = 1

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def check_island(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    maps[i][j] = count

    while q:
        x, y = q.popleft()
        

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0 <= ny < N and maps[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                maps[nx][ny] = count

answer = sys.maxsize

def compute_distance(count):
    global answer
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if maps[i][j] == count:
                q.append((i,j))
                dist[i][j] = 0

    while q:
        x, y =q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if maps[nx][ny] > 0 and maps[nx][ny] != count:
                answer = min(answer,dist[x][y])
                return
            
            if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j] == 1:
            check_island(i,j)
            count+=1

for i in range(1,count):
    compute_distance(i)

print(answer)