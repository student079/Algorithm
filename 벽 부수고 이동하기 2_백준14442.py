import sys
from collections import deque

N, M, K = map(int,sys.stdin.readline().split())
board =[list(map(int,sys.stdin.readline().rstrip('\n')))\
         for _ in range(N)]

# bfs를 기본으로하고
# 가려고 하는 방향이 0이면 걍 가고
# visited 유지
# 3차원으로 만들고 z를 K+1만큼 만들어서
# 벽 안부숨, 1개 부숨, 2개 부숨, ...

dx = (0,1,0,-1)
dy = (1,0,-1,0)


visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

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
                if board[nx][ny] == 1 and z < K and visited[nx][ny][z+1] == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append((nx,ny,z+1))
                # 벽이 없을 때
                elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
    
    return -1


print(bfs())