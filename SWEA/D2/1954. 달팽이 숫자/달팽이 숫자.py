T = int(input())
dx = (0,1,0,-1)
dy = (1,0,-1,0)

for t in range(1,T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]

    x,y = 0,0
    k = 0
    for i in range(1,N**2+1):
        board[x][y] = i

        if not (0<=x+dx[k]<N and 0<=y+dy[k]<N) or  board[x+dx[k]][y+dy[k]] != 0:
            k = (k+1)%4
        x += dx[k]
        y += dy[k]

    print("#" + str(t))
    for i in board:
        print(*i)