from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 내부는 0으로 테두리는 1로 채우기
    # 인접한 테두리 최단거리를 위해 *2
    
    board = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2+ 1):
                # 내부 0
                if x1<i<x2 and y1<j<y2:
                    board[i][j] = 0
                # 내부 아니면서 테두리 일때
                elif board[i][j] != 0:
                    board[i][j] = 1
                    
    dx = (0, 1, 0 , -1)
    dy = (1, 0, -1, 0)
    
    # BFS
    q = deque()
    q.append((characterX*2, characterY*2))
    visited = [[-1] * 102 for _ in range(102)]
    visited[characterX*2][ characterY*2] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] // 2
            break
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if board[nx][ny] == 1 and (visited[nx][ny] == -1 
                                       or visited[nx][ny] > 1 + visited[x][y]):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
            
    return answer