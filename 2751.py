import sys

num = int(input())

lst = []

for _ in range(num):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in lst:
    print(i)
