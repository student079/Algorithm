# 시간복잡도
# 누적합

def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    # 누적합 배열 만들기
    s = [[0] * (M+1) for _ in range(N+1)]
    for type, r1,c1,r2,c2, deg in skill:
        if type == 1:
            deg = -deg
        s[r1][c1] += deg
        s[r1][c2+1] += -deg
        s[r2+1][c1] += -deg
        s[r2+1][c2+1] += deg
    
    # 건물과 연산할 누적합 배열 펼치기
    # 행기준
    for i in range(N+1):
        for j in range(1, M+1):
            s[i][j] += s[i][j-1]
    
    # 열기준
    for i in range(M+1):
        for j in range(1, N+1):
            s[j][i] += s[j-1][i]
    
    # 건물과 연산
    for i in range(N):
        for j in range(M):
            if board[i][j] + s[i][j] > 0:
                answer+=1
    
    return answer