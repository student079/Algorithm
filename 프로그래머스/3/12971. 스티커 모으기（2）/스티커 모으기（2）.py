# 100000
# dp 느낌

def solution(sticker):
    N = len(sticker)
    if N <= 2:
        return max(sticker)
    
    # dp 배열 두개로 처음거 먹은 경우 안먹은 경우로 나눠서 마지막
    # 처음거 먹은 경우
    dp1 = [0] * N
    # 처음거 안먹은 경우
    dp2 = [0] * N
    
    dp1[0], dp2[0] = sticker[0], 0
    dp1[1], dp2[1] = sticker[0],sticker[1]
    
    # 처음꺼 먹은 경우
    for i in range(2, N-1):
        # 지금꺼 먹고 이전, 다음꺼 포기
        # 지금꺼 안먹고 이전, 다음꺼 안포기
        dp1[i] = max(dp1[i-2] + sticker[i],dp1[i-1])
    
    # 처음꺼 안먹은 경우
    for i in range(2,N):
         dp2[i] = max(dp2[i-2] + sticker[i],dp2[i-1])

    return max(dp1[N-2], dp2[N-1])