import sys

N, M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

from itertools import permutations

ps = sorted(set(permutations(nums, M)))

for i in ps:
    print(" ".join(map(str, i)))
