import sys

ESM = list(map(int, sys.stdin.readline().rstrip('\n').split()))

x = 1
y = 1
z = 1
year = 1

while (True):
    if x == ESM[0] and y == ESM[1] and z == ESM[2]:
        break
    x += 1
    y += 1
    z += 1
    year += 1
    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1


print(year)
