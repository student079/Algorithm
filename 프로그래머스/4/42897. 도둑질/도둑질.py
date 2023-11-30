def solution(money):
    
    # 딱봐도 DP
    
    # 첫번째 집 털경우
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    # 첫번째 집 안털고 마지막 집 털경우
    dp2 = [0] * len(money)
    dp2[1] =  money[1]
    for i in range(2,len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp), max(dp2))