import sys
from collections import deque

dx = (-2, -2, -1, 1, 2, 2, -1, 1)
dy = (-1, 1, 2, 2, 1, -1, -2, -2)
def bfs():
    while q:
        x, y = q.popleft()
        
        if [x, y] == end:
            return M[x][y]

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            

            if 0 <= nx < L and 0 <= ny < L and not M[nx][ny]:
                M[nx][ny] = M[x][y] + 1
                q.append([nx,ny])

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    M = [[0] * L for _ in range(L)]
    start = list(map(int,sys.stdin.readline().split()))
    end = list(map(int,sys.stdin.readline().split()))

    q = deque()
    q.append(start)

    print(bfs())