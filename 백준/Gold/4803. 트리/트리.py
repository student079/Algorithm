# 유니온 파인드
import sys

idx = 0
while True:
    idx+=1
    N, M = map(int, sys.stdin.readline().rstrip().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 모든 정점에서 내려 오면서 개수 세기
    visited = [False] * (N+1)
    parents = [-1] * (N+1)
    # 사이클 있는지 
    def checkCycle(node):
        for gnode in graph[node]:
            if parents[node] == gnode:
                continue

            if visited[gnode]:
                return False
            
            parents[gnode] = node
            visited[gnode] = True
            
            if not checkCycle(gnode):
                return False
        return True
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            parents[i] = i
            if checkCycle(i):
                cnt+=1
    
    if cnt == 0:
        print("Case {}: No trees.".format(idx))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(idx))
    else:
        print("Case {}: A forest of {} trees.".format(idx, cnt))


    

