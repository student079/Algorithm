# BFS 벽을 최소 몇 개 부수어야 하는가?
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 가중치

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny)) #벽 없는 곳 우선으로 돌기
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
print(dist[n-1][m-1])