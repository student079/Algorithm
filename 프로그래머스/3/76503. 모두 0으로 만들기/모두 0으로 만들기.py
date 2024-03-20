# 2 <= a, edges <= 300,000
# 그래프 -> 트리

import sys

answer = 0
sys.setrecursionlimit(300000)

def solution(a, edges):
    l = len(a)
    
    # a 합이 0이 안되면 -1
    if sum(a) != 0:
        return -1
    
    tree = [[] for _ in range(l)]
    for edge in edges:
        u, v = edge
        tree[u].append(v)
        tree[v].append(u)
        
    # dfs로 leaf 먼저 해주자
    def dfs(idx, visited):
        global answer
        
        visited[idx] = True
        
        for v in tree[idx]:
            if not visited[v]:
                dfs(v, visited)
                
                a[idx] += a[v]
                answer += abs(a[v])
                a[v] = 0
        
    visited = [False] * l
    dfs(0, visited)

    return answer