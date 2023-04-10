#pypy3 채점

import sys

N, M = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(str,sys.stdin.readline().rstrip('\n'))))

dx = (0,1,0,-1)
dy = (1,0,-1,0)

answer = False
def dfs(i,j,step, visited,start,color):
    global answer

    #조기 종료 조건을 걸어야할듯


    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]

        if 0 <= di < N and 0 <= dj < M and board[di][dj] == color:
            if visited[di][dj]:
                if step >= 4 and (di,dj) == start:
                    answer = True
                    return
            else:
                visited[di][dj] = True
                dfs(di,dj,step + 1,visited,start,color)
                visited[di][dj] = False

visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,1, visited,(i,j),board[i][j])
        if answer:
            print("Yes")
            exit()
else:
    print("No")