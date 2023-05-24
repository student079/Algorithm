import sys
from collections import deque

N = int(sys.stdin.readline())
ip = list(map(int,sys.stdin.readline().split()))
src = (ip[0],ip[1])
dst = (ip[2],ip[3])

# dfs로 가능할 듯하다
# 갈수있는 곳은 다 방문
# 방문 한 곳은 방문 처리
# ans가 그대로 이면 -1

dx = (-2,-2,0,0,2,2)
dy = (-1,1,-2,2,-1,1)
board = [[-1] * N for _ in range(N)]
ans = 201

def dfs(board,i,j,cnt):
    global ans
    # 조기 종료
    if cnt > ans:
        return
    
    # 결과
    if (i,j) == dst:
        ans = min(ans,cnt)
        return
    
    for k in range(6):
        nx = i + dx[k]
        ny = j + dy[k]

        # 보드 밖
        if not (0<=nx<N and 0<=ny<N):
            continue
        
        # 아직 한번도 방문 안했거나 방문 cnt가 작아질 수 있는 것들
        if board[nx][ny] == -1 or board[nx][ny] > cnt:
            board[nx][ny] = cnt
            dfs(board,nx,ny,cnt+1)
    
board[src[0]][src[1]] = 0
dfs(board,src[0],src[1],0)
if ans == 201:
    print(-1)
else:
    print(ans)