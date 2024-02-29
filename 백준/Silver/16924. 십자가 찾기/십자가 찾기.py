import sys

N, M = map(int, sys.stdin.readline().split())

# visited 기록해서 같은지

board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

visited = [['.'] * M for _ in range(N)]
res = []
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def check(x, y):
    cnt = 0
    flag = True
    
    while flag:
        for k in range(4):
            nx = x + dx[k] * (cnt + 1)
            ny = y + dy[k] * (cnt + 1)

            if not (0<=nx<N and 0<= ny<M):
                flag = False
                break

            if board[nx][ny] != '*':
                flag = False
                break
        else:
            cnt += 1

    return cnt

def visit(i,j,cnt):
    visited[i][j] = '*'
    for c in range(cnt):
        for k in range(4):
            x = i + dx[k] * (c + 1)
            y = j + dy[k] * (c + 1)

            visited[x][y] = '*'

for i in range(N):
    for j in range(M):
        if board == visited:
            print(len(res))
            for r in res:
                print(*r)
            exit(0)

        if board[i][j] == '*':
            cnt = check(i,j)
            if cnt > 0:
                res.append((i+1, j+1, cnt))
                visit(i,j,cnt)

print(-1)