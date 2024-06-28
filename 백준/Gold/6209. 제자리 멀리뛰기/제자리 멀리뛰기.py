# n개의 작은 돌섬들 중 m개를 제거
# 돌섬을 점프한 거리의 최솟값을 최대한 크게 
# 두 돌섬이 아무리 멀더라도 점프할 수 있다.
# n-m개의 모든 돌섬을 밟으면서 탈출
# 이진탐색

import sys

d, n, m = map(int ,sys.stdin.readline().rstrip().split())
stones = []
for _ in range(n):
    stones.append(int(sys.stdin.readline()))
stones.sort()

left = 0
right = d

while left <= right:
    mid = (left + right)//2
    stoneCnt = 0
    now = 0

    # 탐색하면서 최소 거리 보다 작으면 cnt 증가
    for s in stones:
        if s - now >= mid:
            now = s
        else:
            stoneCnt += 1
    
    if stoneCnt > m:
        right = mid - 1
    else:
        left = mid + 1

print(right)