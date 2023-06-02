import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(N)]

# 0을 찾아서 인접한 0들의 개수를 음수로 보드에 저장
# 이걸 bfs로하고
# 보드 한번더 돌면서 1이면 상하좌우에 1이 아닌 부분의 값에 절대값 씌워서 더하기
# -> X
# 인접한 0들은 한번만 더해야함
# dic로 바꾸자

dx = (0,1,0,-1)
dy = (1,0,-1,0)
idx = 2
zeroD = dict()

def zero(i,j):
    global idx 

    q = deque()
    q.append((i,j))

    cnt = 1
    board[i][j] = -1
    group = set() # 방문한 곳들 모아서 같은 인덱스로 저장
    group.add((i,j))
    while q:
        x,y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue

            if board[nx][ny] == 0:
                q.append((nx,ny))
                board[nx][ny] = -1
                group.add((nx,ny))
                cnt += 1
    
    # 딕셔너리에 0개수 저장하고 보드에는 인덱스 저장
    zeroD[idx] = cnt 
    for k in group:
        board[k[0]][k[1]] = idx
    idx += 1
    
    return

# 상하좌우 값 더해주기
def plus(x,y):
    cnt = board[x][y]
    visited = set()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= N or ny <0 or ny >= M:
            continue
        idx = board[nx][ny]
        if idx > 1 and idx not in visited:
            cnt += zeroD[idx]
            visited.add(idx)

    return cnt


# 인접한 0 개수 딕셔너리에 저장하기
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero(i,j)

# 1인부분의 상하 좌우 보면서 딕셔너리 참고해서 더해주기
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            print(plus(i,j)%10,end="")
        else:
            print("0",end="")
    print()