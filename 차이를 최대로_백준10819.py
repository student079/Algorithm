import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

res = 0
for i in permutations(nums):
    s = 0
    for j in range(N - 1):
        s += abs(i[j] - i[j + 1])
    if s > res:
        res = s

print(res)