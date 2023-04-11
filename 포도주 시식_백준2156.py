import sys

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = nums[i]
    elif i == 1:
        dp[i] = nums[0] + nums[1]
    elif i == 2:
        dp[i] =  max(nums[0] + nums[1],nums[0] + nums[2], nums[1] + nums[2])
    else:
        dp[i] = max(dp[i-1], dp[i-2] + nums[i],dp[i-3] + nums[i-1] + nums[i])
        #이전에 두개 연속, 이전에 

print(dp[n-1])