# 회전, 대칭
# N, M 4 ~ 500
# 250000 이십오만 * 나올 수 있는 도형 개수 19개
# 4750000 5백만 가능
# 다 돌면서 도형에 넣기

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 도형
one = [((0 ,0), (0, 1), (0, 2), (0, 3)), ((0,0), (1, 0), (2, 0), (3, 0))] # 2개
two = [((0, 0), (0, 1), (1, 0), (1, 1))] # 1개
three = [((0 ,0), (1, 0), (2, 0), (2, 1)), ((0,0), (1,0 ), (2,0), (2, -1)),
         ((0,0), (1, 0), (0,1), (0, 2)), ((0,0), (1,0), (1,1),(1,2)),
         ((0,0), (0,1), (1,1), (2,1)), ((0,0), (1, 0), (2, 0), (0,1)),
         ((1,0), (1,1), (1,2), (0,2)), ((0,0), (0,1), (0,2), (1,2))] # 8개
four = [((0, 0), (1, 0), (1, 1), (2, 1)), ((0,1), (1,1), (1, 0), (2,0)),
        ((1,0), (1, 1), (0,1), (0,2)), ((0,0), (0,1), (1,1), (1, 2))] #  4개
five = [((0, 0), (0, 1), (0, 2), (1, 1)), ((1,0), (0,1), (1,1), (2, 1)),
        ((0,1), (1,0), (1,1), (1, 2)), ((0,0), (1,0), (2, 0), (1, 1))] #  4개

tt = []
for i in one:
    tt.append(i)
for i in two:
    tt.append(i)
for i in three:
    tt.append(i)
for i in four:
    tt.append(i)
for i in five:
    tt.append(i)

answer = 0

def check(i, j):
    global answer
    for t in tt:
        s = 0
        for k in t:
            ni = i + k[0]
            nj = j + k[1]

            if not ( 0<= ni < N and 0 <= nj < M):
                break

            s += board[ni][nj]
        answer = max(answer, s)

for i in range(N):
    for j in range(M):
        check(i, j)

print(answer)