import sys
from math import ceil
# N <= 100

count = 0
N, K = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split()))]
dx = (0 ,1, 0, -1)
dy = (1, 0, -1, 0)

def accountFish(board):
    newBoard = []

    # 쌓기
    w = len(board[1])
    newBoard.append(board[0][w:])

    # 회전 (0 ~ w-1)
    for k in range(w-1,-1,-1):
        temp = []
        for h in range(len(board)):
            temp.append(board[h][k])
        newBoard.append(temp)

    return newBoard

def adjustFish(board):
    h = len(board)
    newBoard = []
    visited = []
    for i in range(h):
        newBoard.append(board[i][:])
        visited.append([False] * len(board[i]))

    for i in range(h):
        w = len(board[i])
        for j in range(w):
            visited[i][j] = True

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if not (0 <= ni < h):
                    continue

                if not ( 0 <= nj < len(board[ni])):
                    continue

                d = abs(board[ni][nj] - board[i][j]) // 5
                if not visited[ni][nj] and d > 0:
                    if board[ni][nj] - board[i][j] > 0:
                        newBoard[ni][nj] -= d
                        newBoard[i][j] += d
                    else:
                        newBoard[ni][nj] += d
                        newBoard[i][j] -= d

    return newBoard

def accountFish2(board):
    newBoard = []

    w = len(board[0])//2
    h = len(board)
    for i in range(h):
        newBoard.append(board[i][w:])

    for i in range(h-1,-1,-1):
        newBoard.append(board[i][:w][::-1])

    return newBoard


while True:
    # 최대 최소 체크
    fishMax = max(board[0])
    fishMin = min(board[0])

    if fishMax - fishMin <= K:
        print(count)
        break

    # 물고기 넣기
    for i in range(N):
        if fishMin == board[0][i]:
            board[0][i] += 1

    # 어항 쌓기 ( 안될때까지)
    board.append([board[0].pop(0)])

    while True:
        board = accountFish(board)
        if ceil(len(board[0])/2) < len(board):
            break
    # 물고기 수 조절
    board = adjustFish(board)

    # 바닥에 놓기
    h = len(board)
    w = len(board[1])
    newBoard = [[]]
    for i in range(len(board[0])):
        for j in range(h):
            if i < w:
                newBoard[0].append(board[j][i])
            else:
                newBoard[0].append(board[0][i])
                break

    # 어항 쌓기 2
    newBoard = accountFish2(newBoard)
    newBoard = accountFish2(newBoard)

    # 물고기 수 조절
    newBoard = adjustFish(newBoard)

    # 일렬로 놓기
    h = len(newBoard)
    w = len(newBoard[1])
    board = [[]]
    for i in range(len(newBoard[0])):
        for j in range(h):
            if i < w:
                board[0].append(newBoard[j][i])
            else:
                board[0].append(newBoard[0][i])
                break

    count += 1