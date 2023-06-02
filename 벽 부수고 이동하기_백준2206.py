import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
board =[list(map(int,sys.stdin.readline().rstrip('\n')))\
         for _ in range(N)]

# bfs를 기본으로하고
# 가려고 하는 방향이 0이면 걍 가고
# 1이면 breakWall = False에서 True로 바꾸어 주고 가기
# 즉, breakWall이 True면 벽 이미 한번 부순거라 못 부수고
# False면 한번 부수고 가보고
# visited 유지
# breakWall을 큐에 넣어야함
# visited를 3차원으로 해서
# 벽을 부수었을 경우랑 안부쉈을 경우를 나누자

dx = (0,1,0,-1)
dy = (1,0,-1,0)


visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        x, y, z= q.popleft()

        if x == N-1 and y == M - 1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<N and 0<=ny<M:
                # 벽이 있고 부술수 있을 떄
                if board[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.append((nx,ny,1))
                # 벽이 없을 때
                elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
    
    return -1


print(bfs())