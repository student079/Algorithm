import sys
sys.setrecursionlimit(10**6)
dx = (1,0,-1,0,1,-1,1,-1)
dy = (0,-1,0,1,1,-1,-1,1)

count = 0
def dfs(i,j):
    global count

    count += 1
    island[i][j] = 0

    for k in range(8):
        if 0<= i+dx[k] < h and 0<= j+dy[k] <w and island[i+dx[k]][j+dy[k]]:
            dfs(i+dx[k],j+dy[k])


while True:
    res = 0
    w, h = map(int,sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    island = []
    for _ in range(h):
        island.append(list(map(int,sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if island[i][j]:
                dfs(i,j)
                if count > 0:
                    res += 1
                    count = 0
    
    print(res)
