import sys

# 백준 1285 동전 뒤집기

# 20 * 20
# 비트마스크

# 가로 비스마스크로 모든 경우의수
# 그에 따른 세로 많이 바뀌는 열로 뒤집기

N = int(sys.stdin.readline())
answer = N * N + 1
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

for rows in range(1<<N):
    temp = [board[i][:] for i in range(N)]
    for i in range(N):
        if rows & (1<<i):
            for j in range(N):
                if temp[i][j] == 'H':
                    temp[i][j] = 'T'
                else:
                    temp[i][j] = 'H'
    # 열 검사
    total = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if temp[j][i] == 'T':
                cnt+=1
        total += min(cnt, N-cnt)
    
    answer = min(answer, total)

print(answer)
        

