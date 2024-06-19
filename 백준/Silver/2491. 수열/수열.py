import sys
# N 100000
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 증가, 감소하는 수열 길이
ans = 2
temp = nums[0]
if N == 1:
    ans = 1

cntA = 1
cntD = 1
for num in nums[1:]:

    # 증가
    if num >= temp:
        cntA += 1
    else:
        cntA = 1
    
    if num <= temp:
        cntD += 1
    else:
        cntD = 1
    temp = num
    ans = max(ans,cntA,cntD)

# 감소


print(ans)