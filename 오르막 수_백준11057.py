import sys

N = int(sys.stdin.readline())

ascending = [[0] * 10 for _ in range(N+1)] 

for i in range(10):
    ascending[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        ascending[i][j] = sum(ascending[i-1][:j+1])

print(sum(ascending[N])%10007)