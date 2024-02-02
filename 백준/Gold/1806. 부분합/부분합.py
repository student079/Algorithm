# 투 포인터

# N 10000

import sys

N, S = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
answer = sys.maxsize

sum = 0
left = 0
right = 0

while True:
    if sum >= S:
        answer = min(answer, right - left)
        sum -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum += nums[right]
        right += 1

print(0 if answer == sys.maxsize else answer)