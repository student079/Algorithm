# 양옆에 자신보다 높은 블록으로 둘러싸여있어야함

import sys
H, W = map(int,sys.stdin.readline().split())
heights = list(map(int,sys.stdin.readline().split()))
ans = 0

for i in range(1,W-1):
    left = max(heights[:i])
    right = max(heights[i+1:])

    diff = min(left,right) - heights[i]

    if diff > 0:
        ans += diff

print(ans)