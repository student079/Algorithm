import sys

# input
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

# with DP algorithm
dp = [0] * N
dp[0] = nums[0]

for i in range(N):
    for j in range(i):
        # if increase
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        # if not inc
        else:
            dp[i] = max(dp[i], nums[i])

print(max(dp))
