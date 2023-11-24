def solution(alp, cop, problems):
    
    # 최단시간
    # DP
    
    # 필요한 알고력, 코딩령
    max_alp = max([i[0] for i in problems])
    max_cop = max([i[1] for i in problems])
    
    # 최소
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    
    # 초기 필요한 시간 0
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop + 1):
            if i < max_alp : 
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop :
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            # 현 상태에서 문제 선택해서 높이는 것
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    #최대 넘으면 index 오류
                    new_alp = min(max_alp, alp_rwd+i)
                    new_cop = min(max_cop, j+cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    
    return dp[max_alp][max_cop]