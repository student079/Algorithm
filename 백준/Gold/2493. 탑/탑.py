# N <= 500000

# 스택
# O(n)

import sys

N = int(sys.stdin.readline())
tops = list(map(int,sys.stdin.readline().rstrip().split()))
stack = []
res = []

for i in range(N):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()

    if not stack:
        res.append(0)
    else:
        res.append(stack[-1][0])
    
    stack.append((i+1, tops[i]))
    
print(*res)
    


