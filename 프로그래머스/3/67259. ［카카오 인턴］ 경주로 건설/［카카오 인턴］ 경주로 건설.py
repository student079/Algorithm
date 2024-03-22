import heapq

dx = (0 ,1, 0, -1)
dy = (1, 0, -1, 0)

def solution(board):
    answer = float("INF")
    bLen = len(board)
    visited = [[[-1] * bLen for _ in range(bLen)] for _ in range(4)]
    
    q = []
    heapq.heappush(q,(0, -1, (0, 0))) #cost, direction, xy
    for i in range(4):
        visited[i][0][0] = 0
    
    while q:
        cost, direction, xy = heapq.heappop(q)
        
        x, y = xy
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if not (0<=nx<bLen and 0<=ny<bLen) or board[nx][ny] == 1:
                continue
            
            s = cost + (100 if direction == k or direction == -1 else 600)
            if visited[direction][nx][ny] == -1 or visited[direction][nx][ny] >= s:
                visited[direction][nx][ny] = s
                heapq.heappush(q,(s, k, (nx,ny)))
    
    for i in range(4):
        if visited[i][bLen-1][bLen-1] != -1:
            answer = min(visited[i][bLen-1][bLen-1], answer)
    
    return answer