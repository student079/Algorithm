import sys

board = []
for _ in range(9):
    board.append(list(map(int,sys.stdin.readline().split())))
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

def rowCheck(i,k):
    if k in board[i]:
        return False
    return True

def colCheck(j,k):
    if k in [w[j] for w in board]:
        return False
    return True

def sqCheck(i,j,k):
    ni = (i//3) * 3
    nj = (j//3) * 3
    temp = []
    for y in range(ni,ni+3):
        for x in range(nj,nj+3):
            temp.append(board[y][x])
    if k in temp:
        return False
    return True

def dfs(n):
    if n == len(blank):
        for i in board:
            print(*i)
        exit(0)
    
    temp = blank[n]
    for num in range(1,10):
        if rowCheck(temp[0],num) and colCheck(temp[1],num) and sqCheck(temp[0],temp[1],num):
            board[temp[0]][temp[1]] = num
            dfs(n+1)
            board[temp[0]][temp[1]] = 0

dfs(0)

