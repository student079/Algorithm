import sys
from collections import deque


# 8*8이라 브르투포스 가능할듯
# 대각선 까지 이동가능 -> 가만히 있을 수도 있음
# 캐릭터가 이동할 수 없는 곳 -> 벽 좌표, 벽좌표 x+1, 체스판 밖
# bfs로 탐색

# 벽 좌표들 받기
walls = [list(sys.stdin.readline().rstrip('\n')) for _ in range(8)]

dx = (0,1,0,-1, 1,1,-1,-1,0)
dy = (1,0,-1,0,1,-1,-1,1,0)

def bfs():
    q = deque()
    q.append((7,0)) # 초기 플레이어 위치
    walls[7][0] = '1'

    while q:
        for _ in range(len(q)): # 벽 내려가는 거 계산
            x,y = q.popleft()

            # 벽 내려와서 덮침
            if walls[x][y] == '#':
                continue

            if x == 0 and y == 7:
                return 1

            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    continue
                
                # 벽 지금 위치만 체크
                # 벽 내려가는 것도 체크 할까?
                # 그냥 그래프로 받아서 탐색하는거 O(1)로 하는 게 낫겠다.
                if walls[nx][ny] != '#' and walls[nx][ny] != '1':
                    q.append((nx,ny))
                    walls[nx][ny] = '1'
                
                if x == nx and y == ny:
                    q.append((nx,ny))
        
        # 벽 내리기
        # 벽 내려가야 하니까 밑에 부터 탐색
        for i in range(7,-1,-1):
            for j in range(8):
                if walls[i][j] == '#':
                    if i+1 < 8:
                        walls[i+1][j] = "#"
                        walls[i][j] = '.'
                    else:
                        walls[i][j] = '.'

    return 0


print(bfs())