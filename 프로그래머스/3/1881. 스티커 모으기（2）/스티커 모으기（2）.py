# 완전탐색 2 ** 100000 불가능
# dp

def solution(sticker):
    answer = 0
    stickerLen = len(sticker)
    
    if stickerLen == 1:
        return sticker[0]
    
    dp = [[0] * stickerLen for _ in range(2)]
    
    # 첫번째 뜯는 경우
    dp[0][0] = sticker[0]
    dp[0][1] = dp[0][0]
    
    for i in range(2, stickerLen - 1):
        dp[0][i] = max(dp[0][i-1], dp[0][i-2] + sticker[i])
    
    
    # 첫번째 안뜯는 경우
    dp[1][1] = sticker[1]
    for i in range(2, stickerLen):
        dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])
    
    return max(max(dp[0]), max(dp[1]))