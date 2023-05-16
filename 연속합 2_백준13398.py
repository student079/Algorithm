import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

# 입력 범위가 100,000까지이기 때문에 한번 돌 때 다 해야해
# dp 사용
# dp[0][i] = 원소제거 안 했을 때
# dp[1][i] = 원소제거 했을 때
dp = [[i for i in nums] for _ in range(2)]

for i in range(1,n):
    # 지금까지+지금 vs 지금
    dp[0][i] = max(dp[0][i-1]+nums[i], nums[i])

    # 이번 요소를 제거 vs 이미 전에 제거
    dp[1][i] = max(dp[0][i-1],dp[1][i-1]+nums[i])

print(max(dp[0]+dp[1]))