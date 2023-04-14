import sys
from collections import deque

S = int(sys.stdin.readline())
visited = dict()
def bfs():
    q = deque()
    q.append((1,0))
    visited[(1,0)] = 0

    while q:
        x, c = q.popleft()
        if x == S:
            print(visited[(x,c)])
            break
        if (x,x) not in visited.keys():
            visited[(x,x)] = visited[(x,c)] + 1
            q.append((x,x))
        if (x+c,c) not in visited.keys():
            visited[(x+c,c)] = visited[(x,c)] + 1
            q.append((x+c,c))
        if (x-1,c) not in visited.keys():
            visited[(x-1,c)] = visited[(x,c)] + 1
            q.append((x-1,c))

bfs()
            
            