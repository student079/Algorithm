# string 활용

import sys
import string

base = string.digits+string.ascii_uppercase


def to_base(N, B):
    res = ""
    while N >= B:
        res = base[N % B] + res
        N //= B
    res = base[N] + res
    return res


N, B = map(int, sys.stdin.readline().strip("\n").split())

print(to_base(N, B))
