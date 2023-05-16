import sys

N = int(sys.stdin.readline())
house = []
for _ in range(N):
    house.append(list(map(int,sys.stdin.readline().split())))

# 시간 0.5초에 N이 1000까지
# dp 사용
# house를 업데이트 하면서 0번째를 선택했다면 1,2중에 작은 거
# 1을 선택했다면 0,2 중에 작은 거
# 마지막에는 첫번째꺼랑 달라야함 
# 첫번째 컬러 별로 구하자 
INF = 10**6 + 1 # 최대값
dp = [[-1] * 3 for _ in range(N)]
ans = INF
for color in [0,1,2]:
    # color 선택하도록
    dp[0] = [INF,INF,INF]
    dp[0][color] = house[0][color]

    for i in range(1,N):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + house[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + house[i][2]

    # color 선택하지 않도록
    dp[N-1][color] = INF
    ans = min(ans,min(dp[N-1]))

print(ans)