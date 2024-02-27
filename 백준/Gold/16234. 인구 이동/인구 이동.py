import sys
from collections import deque

N, L, R = map(int,sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = (0, 1, 0 ,-1)
dy = (1, 0, -1, 0)


def findAndMove(visited, i,j):
    visited[i][j] = 1

    q = deque()
    q.append((i,j))
    contries = set()
    contries.add((i,j))
    cnt = 1
    s = 0
    s += A[i][j]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (0<=nx<N and 0<=ny<N):
                continue

            if visited[nx][ny] == 0 and (L <= abs(A[x][y] - A[nx][ny]) <= R):
                visited[nx][ny] = 1
                q.append((nx,ny))
                s += A[nx][ny]
                cnt += 1
                contries.add((nx,ny))
    
    if cnt == 1:
        return False
    
    # move
    res = s // cnt
    for p in contries:
        a, b = p
        A[a][b] = res

    return True


ans = 0
while True:

    visited = [[0] * N for _ in range(N)]

    ctn = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                check = findAndMove(visited, i,j)
                if not ctn and check:
                    ctn = True
    
    if not ctn:
        break

    ans += 1

print(ans)