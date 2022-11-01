# 나머지 활용

import sys

n, k = map(int, sys.stdin.readline().split())

lst = []
result = []
for i in range(1, n+1):
    lst.append(i)


def back(lst):
    if len(lst) == 0:
        return -1
    else:
        return len(lst)-1


idx = 0
while lst:
    idx += k-1
    if idx >= len(lst):
        idx = idx % len(lst)

    result.append(lst.pop(idx))


print("<", ", ".join(str(i) for i in result), ">", sep="")
