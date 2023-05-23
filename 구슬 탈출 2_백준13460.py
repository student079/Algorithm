import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip('\n')))

# B,R 좌표 각각 찾고
# 같이 bfs 돌리면서 찾기
# count가 10 넘으면 -1 출력
# R만 O에 들어가야함 -> B랑 같은 좌표에 있으면 넘어감
# #은 벽이니까 벽전까지 가야함 혹은 다른구슬 전까지
# R이 홀에 들어갈때 같이 B도 들어가면 안댐

visited = set()

# 처음 구슬들 위치 반환
def getXY():
    b = 0
    r = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'B':
                b = (i,j)
            elif board[i][j] == 'R':
                r = (i,j)
            if b != 0 and r != 0:
                return b,r

dx = (0,1,0,-1)
dy = (-1,0,1,0)

# 벽이나 구멍 만날때까지 움직인 좌표 반환
def move(x,y,dx,dy):
    dis = 0 # 구슬 겹치면 거리 적은 구슬 한칸 뒤로하기 위해
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        dis += 1
    return x,y,dis

def bfs():
    q = deque()
    q.append((blue,red,0))

    while q:
        b, r, cnt = q.popleft()

        if cnt >= 10:
            print(-1)
            exit()

        for k in range(4):
            nBx, nBy, Bdis = move(b[0],b[1],dx[k],dy[k])
            nRx, nRy, Rdis = move(r[0],r[1],dx[k],dy[k])

            # 파란구슬이 들어가면 그냥 넘김
            if board[nBx][nBy] == 'O':
                continue

            if board[nRx][nRy] == 'O':
                print(cnt+1)
                exit()

            # 두 구슬이 겹쳤을 때 거리보고 긴걸 한번 바꾸
            if nBx == nRx and nBy == nRy:
                if Bdis > Rdis:
                    nBx -= dx[k]
                    nBy -= dy[k]
                else:
                    nRx -= dx[k]
                    nRy -= dy[k]

            # 방문기록확인
            visit = (nBx,nBy,nRx,nRy)
            if visit not in visited:
                visited.add(visit)
                q.append(((nBx,nBy),(nRx,nRy),cnt+1))


# 각각 좌표 찾아주기
blue, red = getXY()
ans = -1
visited.add((blue[0],blue[1],red[0],red[1]))
bfs()
print(ans)