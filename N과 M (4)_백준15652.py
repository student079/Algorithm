import sys
from itertools import combinations_with_replacement

N, M = map(int,sys.stdin.readline().split())

for i in combinations_with_replacement(range(1,N+1), M):
    for j in i:
        print(j, end=" ")
    print()