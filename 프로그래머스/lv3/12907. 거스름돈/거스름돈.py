def solution(n, money):
    
    #딱봐도 dp같은데
    
    # 다시 풀어보기
    dp = [1] + [0] * n
    
    for i in money:
        for j in range(i, n+1):
            if j >= i:
                dp[j] += dp[j - i]
                
    return dp[n]