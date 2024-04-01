# x <= 999999
# 6!

import sys
from itertools import permutations

X = sys.stdin.readline().rstrip()
candidates = sorted(list(permutations(X)), reverse=True)
X = int(X)
same = -1

for i in range(len(candidates)):
    num = int("".join(candidates[i]))
    if num == X:
        same = i
        break

if same == -1 or same == 0:
    print(0)
else:
    print(int("".join(candidates[same-1])))