from itertools import product

N, M = map(int,input().split())
nums = list(map(int,input().split()))

for i in product(sorted(nums),repeat = M):
    stack = []
    for j in i:
        stack.append(j)
    else:
        for k in stack:
            print(k, end=" ")
    print()