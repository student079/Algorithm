from collections import deque

def solution(board):
    global answer
    answer = 0
    
    # 위에 블럭 있는지 체크
    def can_delete(x,y):
        for k in range(x+1):
            if board[k][y] != 0:
                return False
        return True
    
    # 제거할 수 있으면 제거하고 카운트 증가
    def delete(k, xy):
        global answer
        
        dx = (0,1,0,-1)
        dy = (1,0,-1,0)
        
        q = deque()
        q.append(xy)
        block = set()
        block.add(xy)
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0 <= nx < N) or not (0 <= ny < N):
                    continue
                
                if board[nx][ny] == k and (nx,ny) not in block:
                    block.add((nx,ny))
                    q.append((nx,ny))
        
        # 빈칸 두칸 찾기
        y = sorted(list(block), key = lambda x:x[1])
        x = sorted(list(block))
        x_min, x_max = x[0][0], x[3][0]
        y_min, y_max = y[0][1], y[3][1]
        
        can = True
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max+1):
                if (i,j) not in block and not can_delete(i,j):
                    can = False
        if can:
            for t in block:
                board[t[0]][t[1]] = 0
            return True
        return False
                
    
    N = len(board)
    
    # 서치하는데 제거할 수 있는 직사각형이 있는지
    # 없으면 현재까지 제거한 횟수 반환
    # 있으면 서치
    
    # 제거할 수 있는 직사각형의 판별
    # BFS로 좌표들 구하고
    # y길이 x길이 구해서 가능한지
    flag = True
    while flag:
        flag = False
        for i in range(N):
            for j in range(N):
                k = board[i][j]
                if k != 0 :
                    f = delete(k, (i,j))
                    if f:
                        answer += 1
                        
                    if f or flag:
                        flag = True
    
    
    return answer