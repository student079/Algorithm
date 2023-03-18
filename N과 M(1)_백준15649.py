import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().rstrip('\n').split())

for i in permutations(range(1,N+1),M):
    for j in i:
        print(j, end=" ")
    print()