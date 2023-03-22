import sys

N, M = map(int,sys.stdin.readline().split())
nums = set(map(int,sys.stdin.readline().split()))

from itertools import product

for i in sorted(product(nums, repeat = M)):
    print(" ".join(map(str, i)))
