# 다시 풀어보기

def solution(matrix_sizes):
    sizes = len(matrix_sizes)
    dp = [[0 for j in range(sizes)] for i in range(sizes)]
    
    for gap in range(1, sizes) : 
        for s in range(0, sizes-gap) : 
            e = s+gap
            
            candidate = list()
            for m in range(s, e) :
                candidate.append(
                    dp[s][m]+dp[m+1][e]+
                    matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1])
            dp[s][e] = min(candidate)
    
    print(dp)
            
    return dp[0][-1]