import sys
from collections import deque

R, C = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip('\n')) for _ in range(R)]

# 물 bfs 사용
# 고슴도치도 bfs 사용
# 돌은 X
# 다 위치 찾아놓고 bfs에 넣기
# visited 해야 메모리 초과 안남
# 좌표들 찾기
S = 0
wq = deque()    # 물
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            S = (i,j)
        elif board[i][j] == '*':
            wq.append((i,j))

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def bfs():
    sq = deque()    # 도치
    sq.append(S)    # 도치 좌표
    cnt = 0
    
    while sq:
        for _ in range(len(sq)):
            x,y = sq.popleft()

            # 물이 차버리면 버려
            if board[x][y] == '*':
                continue

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                
                if board[nx][ny] == 'D':
                    return cnt+1

                if board[nx][ny] == '.':
                    sq.append((nx,ny))
                    board[nx][ny] = 'S'

        cnt += 1
        for _ in range(len(wq)):
            x,y = wq.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue

                if board[nx][ny] == '.' or board[nx][ny] == 'S':
                    wq.append((nx,ny))
                    board[nx][ny] = '*'
                     
    return "KAKTUS"

print(bfs())
            

