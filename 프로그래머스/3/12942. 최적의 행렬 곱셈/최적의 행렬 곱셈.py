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

# import sys
# def solution(matrix_sizes):
#     answer = 0
#     d = [matrix_sizes[0][0]]
#     for i in range(len(matrix_sizes)):
#         d.append(matrix_sizes[i][1])
#     length = len(d)
#     M = [[0 for x in range(length)] for y in range(length)]
#     for diag in range(1, length):
#         for i in range(1, length-diag):
#             j = i+diag
#             M[i][j] = sys.maxsize
#             for k in range(i,j):
#                 M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j])
#     answer = M[1][length-1]
#     return answer
