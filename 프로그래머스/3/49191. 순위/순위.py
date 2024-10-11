# 

def solution(n, results):
    answer = 0
    
    board = [[0] * (n+1) for _ in range(n+1)]
    
    for win, lose in results:
        board[win][lose] = 1
        board[lose][win] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or board[i][j] != 0:
                    continue
                else:
                    if board[i][k] != 0 and board[i][k] == board[k][j] :
                        board[i][j] = board[i][k]
                        board[j][i] = board[i][k] * -1
    
    for result in board:
        if result.count(0) == 2:
            answer+=1
    return answer