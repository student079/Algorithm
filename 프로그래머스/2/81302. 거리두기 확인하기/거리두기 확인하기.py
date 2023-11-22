from collections import deque

def solution(places):
    answer = []
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    
    def bfs(pos, place):
        visited = [[False] * 5 for _ in range(5)]
        x, y = pos
        visited[x][y] = True
        q = deque()
        q.append((pos, 0))
        while q:
            o_pos, cnt = q.popleft()
            
            
            for k in range(4):
                nx = o_pos[0] + dx[k]
                ny = o_pos[1] + dy[k]
                
                if not (0 <= nx < 5 and 0 <= ny < 5):
                    continue
                    
                if place[nx][ny] != 'X' and not visited[nx][ny]:
                    if place[nx][ny] == 'O':
                        visited[nx][ny] = True
                        q.append(((nx, ny), cnt + 1))
                    elif place[nx][ny] == 'P' and cnt < 2:
                        return 0
                        
        return 1
                    
    
    def check(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs((i,j), place) == 0:
                        return 0
        return 1
    
    for place in places:
        if check(place) == 0:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer