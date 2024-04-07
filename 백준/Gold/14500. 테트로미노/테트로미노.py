import sys

def dfs(x, y, step, total):
    global answer

    # 종료조건1) 보드의 최대값이 더해진다 해도 answer보다 작으면 탐색 종료
    if total + max_val*(4-step) <= answer:
        return
    
    # 종료조건2) 4개 다 봤ㅇ면 종료
    if step == 4:
        answer = max(answer, total)
        return
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 'ㅏ'모양도 봐주기 위해서 두번째 보는 거면 현재에서 다시 dfs호출출
            if step == 2:
                visited[nx][ny] = True
                dfs(x,y,step + 1,total + board[nx][ny])
                visited[nx][ny] = False

            
            visited[nx][ny] = True
            dfs(nx,ny,step+1,total+board[nx][ny])
            visited[nx][ny] = False
    



N,M = map(int,sys.stdin.readline().rstrip('\n').split())

board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))

max_val = max(map(max,board))
answer = 0
d = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False] * M for _ in range(N)] # 탐색여부 확인용
answer = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,1,board[i][j])
        visited[i][j] = False

print(answer)