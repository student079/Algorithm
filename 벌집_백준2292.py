import sys

N = int(sys.stdin.readline().rstrip('\n'))

i = 1
res = 0
while N > 0:
    res += 1
    N -= i
    i =6 * res

print(res)