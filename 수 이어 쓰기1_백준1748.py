import sys

N = sys.stdin.readline().rstrip('\n')

res = 0

digit = len(N)

N = int(N)
for i in range(digit - 1):
    res += 9 * (10 ** i) * (i + 1)

res += (N-(10**(digit-1)) + 1) * digit

print(res)