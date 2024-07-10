# N, M 1~50
# 높이 1~9
# 2500 개 좌표 각각 bfs는 2500

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
# 좌표 bfs
# 하나하나 들어가서 자신보다 작거나 같은 값만 탐색
# 자신보다 큰 값은 벽으로 인식하고 벽중 가장 작은 값 저장 후
# 범위 밖이면 나오기
# 정상적으로 끝났다면 최소벽이랑 지금까지 값들 계산

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def bfs(i, j):
    q = deque()
    value = board[i][j]
    wall = 10
    visited2 = set()
    q.append((i,j))
    visited2.add((i,j))
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                return 0
            
            if board[nx][ny] <= value and (nx,ny) not in visited2:
                q.append((nx,ny))
                visited2.add((nx,ny))
            elif board[nx][ny] > value:
                wall = min(wall,board[nx][ny])
    res = 0
    for x, y in list(visited2):
        res += wall - board[x][y]
        board[x][y] = wall

    return res


answer = 0
for i in range(N):
    for j in range(M):
        answer += bfs(i,j)
print(answer)
