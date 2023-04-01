import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
count = Counter(nums)
stack = []
answer = [-1] * N
for i in range(N):
    while stack and count[nums[stack[-1]]] < count[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)