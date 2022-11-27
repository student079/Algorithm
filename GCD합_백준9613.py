import sys


def gcd(a, b):
    r = a % b
    if r != 0:
        return gcd(b, r)
    else:
        return b


n = int(sys.stdin.readline().rstrip('\n'))

for i in range(n):
    lst = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    sum = 0
    num = lst.pop(0)
    for j in range(num):
        for k in range(j, num):
            sum += gcd(lst[j], lst[k])
        sum -= lst[j]
    print(sum)
