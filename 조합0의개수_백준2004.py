import sys

# 런타임에러 해결->2,5의 짝 하나당 0 하나인것을 이용
# 조합은 n!/(n-r)!r!


def count_n(n, key):
    num = 0
    while n != 0:
        n = n // key
        num += n
    return num


n, m = map(int, sys.stdin.readline().rstrip('\n').split())

two = count_n(n, 2) - count_n(n-m, 2) - count_n(m, 2)
five = count_n(n, 5) - count_n(n-m, 5) - count_n(m, 5)

print(min(two, five))
