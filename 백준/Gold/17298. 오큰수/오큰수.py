import sys

N = int(sys.stdin.readline()) # N 1000000
arr = list(map(int,sys.stdin.readline().rstrip().split()))
res = []
stack = []

arr.reverse()
for i in arr:
    while stack:
        if stack[-1] > i:
            res.append(stack[-1])
            break
        else:
            stack.pop()
    else:
        res.append(-1)
    
    stack.append(i)
res.reverse()
print(*res)