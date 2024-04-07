# 주사위 칸 나타낼 수 있게 (반대 칸 숫자)
# 보드 바깥으로 나가려고 하면 무시

import sys

N, M, x, y, K = map(int,sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
commands = list(map(int,sys.stdin.readline().rstrip().split()))

dx = (0, 0, 0, -1, 1)
dy = (0, 1, -1, 0, 0)
# 동, 서, 북, 남

dice = [0, 0, 0, 0, 0, 0]
# 0 -> 위
# 1 -> 뒤
# 2 -> 오른쪽
# 3 -> 왼쪽
# 4 -> 앞
# 5 -> 바닥
# 동
def east(dice):
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
# 서
def west(dice):
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
# 북
def north(dice):
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
# 남
def south(dice):
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


for command in commands:

    if not ( 0<= x + dx[command] < N and 0 <= y + dy[command] < M):
        continue

    newX = x + dx[command]
    newY = y + dy[command]

    if command == 1:
        east(dice)
    elif command == 2:
        west(dice)
    elif command == 3:
        north(dice)
    else:
        south(dice)

    if board[newX][newY] == 0:
        board[newX][newY] = dice[5]
    else:
        dice[5] = board[newX][newY]
        board[newX][newY] = 0

    print(dice[0])

    x = newX
    y = newY