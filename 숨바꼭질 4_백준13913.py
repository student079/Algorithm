import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
visited = set()
path = [0]*100001
def bfs():
    q = deque()
    q.append((N,0))
    visited.add(N)

    while q:
        x, count = q.popleft()
        if x == K:
            print(count)
            check_path(x,count)
            break
        for i in [x+1,x-1,2*x]:
            if 0<= i <= 100000 and i not in visited:
                visited.add(i)
                q.append((i,count+1))
                path[i] = x

def check_path(x,count):
    arr = []
    temp = x
    for _ in range(count + 1):
        arr.append(temp)
        temp = path[temp]
    print(*(arr[::-1]))

bfs()
