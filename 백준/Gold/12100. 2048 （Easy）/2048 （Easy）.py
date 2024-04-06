# 상하좌우
# 블록이 이미 합쳐졌는지 체크해야해
# 5번 가장 큰 블록
from collections import deque

import sys

N = int(sys.stdin.readline())
board = []
maxBlock = 0
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    maxBlock = max(maxBlock, max(board[i]))
dx = (1, 0, -1, 0)
dy = (0 ,1, 0, -1)
# 하, 우, 상, 좌

q = deque()
q.append((board, 0))
while q:
    oriBoard, cnt = q.popleft()
    if cnt >= 5:
        continue

    for k in range(4):
        # 합쳐진 블록인지 체크
        visited = [[False] * N for _ in range(N)]
        newBoard = []
        for i in range(N):
            newBoard.append(oriBoard[i][:])

        # 하
        if k == 0:
            # N -2 줄 부터 0까지
            for j in range(N):
                for i in range(N-2, -1, -1):
                    if newBoard[i][j] == 0:
                        continue
                    ni = i
                    nj = j
                    while True:
                        ni += dx[k]
                        nj += dy[k]
                        if not ( 0 <= ni < N and 0 <= nj < N):
                            break
                        if newBoard[ni][nj] == 0:
                            newBoard[ni][nj] = newBoard[ni-dx[k]][nj-dy[k]]
                            newBoard[ni - dx[k]][nj - dy[k]] = 0
                            i = ni
                            j = nj
                        else:
                            break
                    if (0 <= ni < N and 0 <= nj < N) and \
                        newBoard[ni][nj] == newBoard[i][j] and not visited[ni][nj]:
                        newBoard[i][j] = 0
                        newBoard[ni][nj] *= 2
                        maxBlock = max(newBoard[ni][nj], maxBlock)
                        visited[ni][nj] = True
            q.append((newBoard, cnt + 1))

        # 우
        elif k == 1:
            # N -2 줄 부터 0까지
            for i in range(N):
                for j in range(N - 2, -1, -1):
                    if newBoard[i][j] == 0:
                        continue
                    ni = i
                    nj = j
                    while True:
                        ni += dx[k]
                        nj += dy[k]
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        if newBoard[ni][nj] == 0:
                            newBoard[ni][nj] = newBoard[ni - dx[k]][nj - dy[k]]
                            newBoard[ni - dx[k]][nj - dy[k]] = 0
                            i = ni
                            j = nj
                        else:
                            break
                    if (0 <= ni < N and 0 <= nj < N) and newBoard[ni][nj] == newBoard[i][j] and not visited[ni][nj]:
                        newBoard[i][j] = 0
                        newBoard[ni][nj] *= 2
                        maxBlock = max(newBoard[ni][nj], maxBlock)
                        visited[ni][nj] = True
            q.append((newBoard, cnt + 1))

        # 상
        elif k == 2:
            # N -2 줄 부터 0까지
            for j in range(N):
                for i in range(1, N):
                    if newBoard[i][j] == 0:
                        continue
                    ni = i
                    nj = j
                    while True:
                        ni += dx[k]
                        nj += dy[k]
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        if newBoard[ni][nj] == 0:
                            newBoard[ni][nj] = newBoard[ni - dx[k]][nj - dy[k]]
                            newBoard[ni - dx[k]][nj - dy[k]] = 0
                            i = ni
                            j = nj
                        else:
                            break
                    if (0 <= ni < N and 0 <= nj < N) and \
                            newBoard[ni][nj] == newBoard[i][j] and not visited[ni][nj]:
                        newBoard[i][j] = 0
                        newBoard[ni][nj] *= 2
                        maxBlock = max(newBoard[ni][nj], maxBlock)
                        visited[ni][nj] = True
            q.append((newBoard, cnt + 1))

        # 좌
        else:
            # N -2 줄 부터 0까지
            for i in range(N):
                for j in range(1,N):
                    if newBoard[i][j] == 0:
                        continue
                    ni = i
                    nj = j
                    while True:
                        ni += dx[k]
                        nj += dy[k]
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        if newBoard[ni][nj] == 0:
                            newBoard[ni][nj] = newBoard[ni - dx[k]][nj - dy[k]]
                            newBoard[ni - dx[k]][nj - dy[k]] = 0
                            i = ni
                            j = nj
                        else:
                            break
                    if (0 <= ni < N and 0 <= nj < N) and \
                            newBoard[ni][nj] == newBoard[i][j] and not visited[ni][nj]:
                        newBoard[i][j] = 0
                        newBoard[ni][nj] *= 2
                        maxBlock = max(newBoard[ni][nj], maxBlock)
                        visited[ni][nj] = True
            q.append((newBoard, cnt + 1))

# 블록 최대값 확인
print(maxBlock)