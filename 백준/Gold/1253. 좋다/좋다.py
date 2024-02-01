# N 2000
# 정렬
# 투 포인터
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
answer = 0

for i in range(N):
    arr = nums[:i] + nums[i+1:]
    left = 0
    right = N - 2

    while left < right:
        res = arr[left] + arr[right]
        if res == nums[i]:
            answer += 1
            break

        if res > nums[i]:
            right -= 1
        else:
            left += 1

print(answer)
        
