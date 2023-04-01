import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

stack = []
answer = [-1] * N

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)