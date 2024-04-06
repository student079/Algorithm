# 사과 먹으면 꼬리 고정
#

import sys
from collections import deque

# 지나간 자기 몸 deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

N = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x - 1][y - 1] = 1

L = int(sys.stdin.readline())
directions = []
for _ in range(L):
    distance, direction = sys.stdin.readline().rstrip().split()
    directions.append((int(distance), direction))

bodys = deque()
bodys.append((0, 0))
k = 0
headX, headY = 0, 0
time = 0

while True:
    time += 1

    newHeadX = headX + dx[k]
    newHeadY = headY + dy[k]

    if not (0 <= newHeadX < N and 0 <= newHeadY < N):
        break

    if board[newHeadX][newHeadY] == 0:
        if (newHeadX, newHeadY) in bodys:
            break
        bodys.popleft()
    else:
        board[newHeadX][newHeadY] = 0

    bodys.append((newHeadX, newHeadY))

    headX = newHeadX
    headY = newHeadY

    if directions and directions[0][0] == time:
        if directions[0][1] == 'L':
            k = (k-1) % 4
        else:
            k = (k+1) % 4
        directions.pop(0)

print(time)


