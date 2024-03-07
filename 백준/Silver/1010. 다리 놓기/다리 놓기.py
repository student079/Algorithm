# 순열
# N ,M <= 30

import sys
from math import factorial

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int,sys.stdin.readline().rstrip().split())

    # mCn
    print(factorial(M) // (factorial(M - N) * factorial(N)))