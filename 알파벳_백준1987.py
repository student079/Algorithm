import sys

# 알파벳 지나온 기록 유지(set)사용 -> 짜피 알파벳 26개니까 배열 26개 생성?
# dfs 사용 count 기록
# 20*20 = 400개
# 시간 초과 방지
# 문제 최대값 이용 + hash사용

ans = 0
dx = (0,1,0,-1)
dy = (1,0,-1,0)

def dfs(record,count,xy):
    global ans

    if count == 26:
        print("26")
        exit()

    ans = max(count,ans)

    for k in range(4):
        nx = xy[0] + dx[k]
        ny = xy[1] + dy[k]
        if 0<= nx<R and 0<=ny<C and not record[ord(board[nx][ny]) - ord('A')]:
            record[ord(board[nx][ny]) - ord('A')] = True
            dfs(record,count+1,(nx,ny))
            record[ord(board[nx][ny]) - ord('A')] = False


R,C = map(int,sys.stdin.readline().split())
board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip('\n')))

record = [False] * 26
record[ord(board[0][0]) - ord('A')] = True
dfs(record,1,(0,0))

print(ans)