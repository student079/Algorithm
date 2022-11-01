import sys

item = int(sys.stdin.readline())

strs = []

for _ in range(item):
    strs.append(sys.stdin.readline().strip())

strs = list(set(strs))

strs.sort(key=lambda x: (len(x), x))

for i in strs:
    print(i)
