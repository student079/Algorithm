import sys

N = int(sys.stdin.readline())
apart = []

for _ in range(N):
    apart.append(list(map(int,sys.stdin.readline().rstrip('\n'))))
answer = []
count = 0

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def dfs(i,j):
    global count

    count += 1
    apart[i][j] = 0
    
    for k in range(4):
        if 0<=i + dx[k]<=N-1 and 0<=j+dy[k]<=N-1 and apart[i+dx[k]][j+dy[k]]:
            dfs(i+dx[k],j+dy[k])

for i in range(N):
    for j in range(N):
        if apart[i][j]:
            dfs(i,j)
            if count:
                answer.append(count)
                count = 0

print(len(answer))
for i in sorted(answer):
    print(i)
            

