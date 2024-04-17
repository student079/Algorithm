# 트럭 한 대로 배송할 수 있는 최대 박스 수
# N 2 ~ 2000
# C 1 ~ 10000
# M 1 ~ 10000
# 받는 마을번호가 보내는 마을 번호보다 큼
# 그리디

import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline())

infos = []
for _ in range(M):
    infos.append((list(map(int, sys.stdin.readline().rstrip().split()))))

infos.sort(key = lambda x: x[1])

boxes = [C] * (N+1)
answer = 0
for a, b, box in infos:
    temp = C
    for i in range(a, b):
        if temp > min(boxes[i], box):
            temp = min(boxes[i], box)
    for i in range(a,b):
        boxes[i] -= temp
    answer += temp

print(answer)