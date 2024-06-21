import math, sys
from itertools import combinations

input = sys.stdin.readline

# N*N 10000
N = int(input())
for _ in range(N):
    answer = -2**31
    nums = list(map(int, input().rstrip().split()))
    cands = list(combinations(nums, 2))
    for a, b in cands:
        answer = max(answer, math.gcd(a,b))
    
    print(answer)
