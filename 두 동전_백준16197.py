import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip('\n')))
dx = (0,1,0,-1)
dy = (1,0,-1,0)
answer = -1

# 동전 위치 찾기
# 초기 위치에서 상하좌우로 같이 움직이는데 #면 안움직임
# bfs쓰는게 좋을듯
# 보드 범위 밖이면 
# 첫번째거 나가고 두번째꺼 검사
# 첫번째거 안나가고 두번째거 나가면 ㄱ
# 둘다 나가는 거는 넘어가
# 10 넘으면 -1

# 동전 위치 찾기
initPlace = []
count = 0 # 두개 다 찾으면 일찍 종료하려고
for i in range(N):
    if count == 2:
            break
    for j in range(M):
        if count == 2:
            break
        if board[i][j] == 'o':
            initPlace.append((i,j))
            count += 1

def bfs(initPlace):
    global answer

    q = deque()
    # 두 동전의 좌표 , count
    q.append((initPlace[0],initPlace[1],0))

    while q:
        coin1, coin2, count = q.popleft()

        # 10이면 bfs이기 때문ㅇ 다른것들도 다 10일거니까 그냥 return
        if count >= 10:
            return
        
        for k in range(4):
            ncoin1 = coin1
            ncoin2 = coin2
            nx1 = coin1[0] + dx[k]
            ny1 = coin1[1] + dy[k]
            nx2 = coin2[0] + dx[k]
            ny2 = coin2[1] + dy[k]

            # 둘다 범위 밖이면 넘어가
            if (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M)\
                and (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M):
                continue

            # 둘중에 하나만 범위 밖이면 종료
            if (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M)\
                and (not (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M)):
                    answer = count+1
                    return
            elif (not (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M))\
                and (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M):
                    answer = count+1
                    return
            
            # 둘다 벽으로 막혀있으면 넘어가
            if board[nx1][ny1] == '#' and board[nx2][ny2] == '#':
                 continue
            # 그게 아니라면 새로 된 좌표 업데이트 해서 큐에 넣어줘
            else:
                if board[nx1][ny1] == '.' or board[nx1][ny1] == 'o':
                    ncoin1 = (nx1,ny1)
                if board[nx2][ny2] == '.' or board[nx2][ny2] == 'o':
                    ncoin2 = (nx2,ny2)
                q.append((ncoin1,ncoin2,count+1))

bfs(initPlace)
print(answer)