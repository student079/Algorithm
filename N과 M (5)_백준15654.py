import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

for i in permutations(sorted(arr),M):
    for j in i:
        print(j, end=" ")
    print()