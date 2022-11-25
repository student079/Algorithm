import sys

stri = sys.stdin.readline().rstrip('\n')

result = [stri]
n = len(stri) - 1
stri = list(stri)
for i in range(n):
    stri.pop(0)
    result.append(''.join(s for s in stri))

for i in sorted(result):
    print(i)
