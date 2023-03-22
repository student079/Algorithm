import sys

N, M = map(int,sys.stdin.readline().split())
nums = sorted(map(int,sys.stdin.readline().split()))

from itertools import combinations

ps = sorted(set(combinations(nums, M)))

for i in ps:
    print(" ".join(map(str, i)))
