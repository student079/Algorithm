# N 1, 1000000 백만

# 총감독관 오직 1명만
# 부감독관은 여러명 가능

# 총 감독관 한명은 꼭 있어야함

import sys
from math import ceil

N = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())
answer = 0

for student in students:
    answer += 1
    rest = student - B
    if rest > 0:
        answer += ceil(rest/C)

print(answer)
