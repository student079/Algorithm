import sys
from collections import deque

A, B, C = map(int,sys.stdin.readline().split())

# dfs로 세개 중에 두개고르는 경우들 중에
# 둘다 0보다 크면 들어가보고
# 종료조건이 중요하겠다
# 만들 수 없는 것을 판단해야함
# 이전과 그대로 인경우  -> visited로 판단 가능
# dfs메모리 초과 + 재귀 깊이 깊다
# bfs로 변경


def bfs():
    visited = set()
    q = deque()

    visited.add((A,B,C))
    q.append([A,B,C])

    while q:
        res = q.popleft()

        if res[0] == res[1] and res[1] == res[2]:
            print("1")
            exit()
    
        res.sort()

        if res[0] != res[1] and (res[0]*2,res[1]-res[0],res[2]) not in visited:
            visited.add((res[0]*2,res[1]-res[0],res[2]))
            q.append([res[0]*2,res[1]-res[0],res[2]])
        if res[0] != res[2] and (res[0]*2,res[1],res[2]-res[0]) not in visited:
            visited.add((res[0]*2,res[1],res[2]-res[0]))
            q.append([res[0]*2,res[1],res[2]-res[0]])
        if res[1] != res[2] and (res[0],res[1]*2,res[2]-res[1]) not in visited:
            visited.add((res[0],res[1]*2,res[2]-res[1]))
            q.append([res[0],res[1]*2,res[2]-res[1]])

bfs()
print("0")


