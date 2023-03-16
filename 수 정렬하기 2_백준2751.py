import sys

N = int(sys.stdin.readline().rstrip('\n'))

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip('\n')))

for i in sorted(arr):
    print(i)