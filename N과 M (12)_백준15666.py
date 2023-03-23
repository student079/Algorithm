import sys
from itertools import combinations_with_replacement

N, M = map(int,sys.stdin.readline().split())
nums = sorted(list(set(map(int,sys.stdin.readline().split()))))

for i in combinations_with_replacement(nums, r=M):
    print(" ".join(map(str,i)))