
# N, M 100, K 50
# 왼쪽과 아래에서만 옴

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline())
board = [[0] * (N + 1) for _ in range(M + 1)]

ends = set()
roads = set()
for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    A = min((b, a), (d, c))
    B = max((b, a), (d, c))
    ends.add(B)
    roads.add((A[0], A[1], B[0], B[1]))

board[0][0] = 1
for i in range(M + 1):
    for j in range(N + 1):
        if i == 0 and j == 0:
            continue

        if (i, j) in ends:
            if (i-1, j, i, j) not in roads:
                board[i][j] = board[i-1][j]
            elif (i, j-1, i, j) not in roads:
                board[i][j] = board[i][j-1]
        else:
            board[i][j] = board[i-1][j] + board[i][j-1]

print(board[M][N])
