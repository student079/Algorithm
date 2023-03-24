import sys
from itertools import permutations

N = int(sys.stdin.readline())

for i in permutations(range(1,N+1), N):
    print(" ".join(map(str, i)))
