import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

for i in combinations(sorted(arr),M):
    for j in i:
        print(j, end=" ")
    print()
