# 다시 풀어보기

def solution(matrix_sizes):
    
    # dp
    # (S~E까지 연산수) = (S~M까지 연산수) + (M+1~E까지의 연산수) + 두 행렬을 곱하기 위한 연산 수
    
    size = len(matrix_sizes)
    dp = [[0] * size for _ in range(size)]
    
    for gap in range(1, size):
        for i in range(size - gap):
            j = i + gap
            
            temp = []
            for k in range(i, j):
                temp.append(dp[i][k]+dp[k+1][j]+ matrix_sizes[i][0]*matrix_sizes[k][1]*matrix_sizes[j][1])
                dp[i][j] = min(temp)
                
    return dp[0][-1]