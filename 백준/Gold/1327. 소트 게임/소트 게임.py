import sys
from collections import deque

N, K = map(int,sys.stdin.readline().rstrip().split()) # 8
arr = list(map(int,sys.stdin.readline().rstrip().split()))

# 완탐
answer = sorted(arr)
res = -1

q = deque()
q.append((arr, 0))
visited = set()
visited.add(tuple(arr))

while q:
    nums, cnt = q.popleft()
    if nums == answer:
        res = cnt
        break

    for i in range(N -K + 1):
        temp = nums[:i] + nums[i:i+K][::-1]+ nums[i+K:]
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            q.append((temp, cnt + 1))

print(res)
