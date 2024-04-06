# 파란구슬 구멍에 들어가면 안됨
# 동시에 둘 다 빠져도 실패
# 구슬 더이상 안움직이면 끝

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
R = 0
B = 0
H = 0
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
dx = (0 ,1, 0, -1)
dy = (1, 0, -1, 0)
# 우 하 좌 상

# 구슬 좌표 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j]
            board[i][j] = '.'
        if board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'
        if board[i][j] == 'O':
            H = [i,j]
        if R != 0 and B != 0 and H != 0:
            break

# BFS로 완전 탐색 최대 40번
# 40 * 100

# 구슬 좌표 따로 저장하고 기울이는 방향에 가까운거 먼저

q = deque()
q.append((R, B, 0))
visited = set()
visited.add((R[0], R[1], B[0], B[1]))
while q:
    r, b, cnt = q.popleft()

    if cnt >= 10:
        continue

    # 방향
    for k in range(4):
        newR = r
        newB = b
        xy = [dx[k], dy[k]]

        distanceR = 0
        distanceB = 0
        while True:
            nextR = [newR[0] + xy[0], newR[1] + xy[1]]
            if board[nextR[0]][nextR[1]] == '.':
                newR = nextR
                distanceR += 1
            else:
                break

        while True:
            nextB = [newB[0] + xy[0], newB[1] + xy[1]]
            if board[nextB[0]][nextB[1]] == '.':
                newB = nextB
                distanceB += 1
            else:
                break

        # 겹치면 더 많이 이동한 곳 한칸 뒤로 빼주기
        if newR == newB:
            if [newR[0] + xy[0], newR[1] + xy[1]] == H:
                continue

            if distanceR > distanceB:
                newR[0] = newR[0] - xy[0]
                newR[1] = newR[1] - xy[1]
            else:
                newB[0]-=xy[0]
                newB[1]-=xy[1]

        if [newB[0] + xy[0], newB[1] + xy[1]] == H:
            continue

        if [newR[0] + xy[0], newR[1] + xy[1]] == H:
            print(cnt+1)
            sys.exit(0)

        if (newR[0], newR[1], newB[0], newB[1]) not in visited:
            visited.add((newR[0], newR[1], newB[0], newB[1]))
            q.append((newR, newB, cnt+1))

print(-1)




