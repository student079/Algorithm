import sys

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    
    matrix = [[INF] * (n+1) for _ in range(n+1)]
                
    for fare in fares:
        x, y, f = fare
        matrix[x][y] = f
        matrix[y][x] = f
    
    # 플로이드 와샬같은데
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    matrix[i][j] = 0
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    answer = sys.maxsize
    for i in range(1, n+1):
        answer = min(answer, matrix[s][i] + matrix[i][a] + matrix[i][b])
    
    return answer