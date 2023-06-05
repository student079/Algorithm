import sys
from collections import deque

N, M, K = map(int,sys.stdin.readline().split())
board =[list(map(int,sys.stdin.readline().rstrip('\n')))\
         for _ in range(N)]

# bfs를 기본으로하고
# 가려고 하는 방향이 0이면 걍 가고
# visited 유지
# visited[x][y]에 벽을 부술 수 있는 개수 저장
# 벽 안부숨, 1개 부숨, 2개 부숨, ...
# 안움직이는 거 추가
# 낮밤이 번갈아 오는데 낮에만 벽 부술 수 있음

dx = (0,1,0,-1)
dy = (1,0,-1,0)


visited = [[K+1] * M for _ in range(N)]

def bfs():
    
    q = deque()
    q.append((0,0,0)) # x,y,벽 부순 횟수
    visited[0][0] = 0
    time = True
    ans = 1

    while q:
        for _ in range(len(q)):

            x, y, w= q.popleft()

            if x == N-1 and y == M - 1:
                return ans

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] <= w:
                        continue
                
                # 벽 있음
                if board[nx][ny] == 1 and w < K:
                    if time:   # 낮
                        visited[nx][ny] = w + 1
                        q.append((nx,ny,w+1))
                    else:           # 밤
                        q.append((x,y,w))
                # 벽이 없을 때
                elif board[nx][ny] == 0:
                    visited[nx][ny] = w
                    q.append((nx,ny,w))
        ans += 1
        time = not time

    return -1


print(bfs())