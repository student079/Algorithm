def solution(money):
    
    # dp
    # 원이기 때문에 첫번째 집 털면 마지막 집 못터니까
    # 두개로 나눠
    # dp[0] : 첫번째 집 터는 경우
    # dp[1] : 첫번째 집 안터는 경우
    l = len(money)
    dp = [[0] * l for _ in range(2)]
    
    # 초기화
    # dp[0]
    dp[0][0] = money[0]
    dp[0][1] = max(money[0],money[1])
    # dp[1]
    dp[1][1] = money[1]
    
    for j in range(2):
        for i in range(2, l-1):
            dp[j][i] = max(dp[j][i-1], dp[j][i-2] + money[i])
    
    # 마지막 집 추가
    dp[1][l-1] = max(dp[1][l-2], dp[1][l-3] + money[l-1])
        
    return max(max(dp[0]), max(dp[1]))