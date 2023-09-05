from collections import deque

def bfs(start, graph, n):
    q = deque([start])
    visited = [0]*(n+1)
    visited[start] = 1
    while q:
        t = q.popleft()
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    return sum(visited)
    

def solution(n, wires):
    
    # 그래프로 받고 BFS로 노드 개수 세기
    # wire 하나씩 짤라보면서 차이 절대값 최소
    answer = n
    
    # 그래프로 받기
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 잘라
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 계산
        t = bfs(a, graph, n)
        answer = min(answer, abs(n - t - t))
        
        #다시 붙이기
        graph[a].append(b)
        graph[b].append(a)
    
    return answer