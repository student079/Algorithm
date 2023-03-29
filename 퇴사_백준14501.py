import sys

N = int(sys.stdin.readline())

table = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    table.append([a,b])

res = 0
visited = [False] * N
def dfs(index, temp, day, forbid):
    global res
    if day == 0:
        if temp > res:
            res = temp
        return
    
    if forbid > 0 or table[index][0] > day:
        dfs(index + 1, temp, day - 1, forbid -1)
    else:
        dfs(index + 1, temp + table[index][1],day -1 ,table[index][0] -1)
        dfs(index + 1, temp, day-1,forbid)


dfs(0, 0, N, 0)
print(res)