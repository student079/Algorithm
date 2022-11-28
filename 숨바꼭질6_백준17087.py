import sys


def gcd(a, b):
    r = a % b
    if r != 0:
        return gcd(b, r)
    else:
        return b


N, S = map(int, sys.stdin.readline().rstrip('\n').split())

bro = list(map(int, sys.stdin.readline().rstrip('\n').split()))

res = abs(bro[0]-S)

for i in range(1, N):
    res = gcd(res, abs(bro[i] - S))

print(res)
