import sys

N = int(sys.stdin.readline().rstrip('\n'))

arr = [1]*10

for _ in range(1, N):
    for i in range(1, 10):
        arr[i] += arr[i-1]

print(sum(arr) % 10007)
