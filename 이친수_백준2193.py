import sys

N = int(sys.stdin.readline().rstrip('\n'))

res = [[0]*2 for _ in range(N+1)]
res[1][0] = 0
res[1][1] = 1

for i in range(2, N+1):
    res[i][0] = res[i-1][1] + res[i-1][0]
    res[i][1] = res[i-1][0]
    # res[i][0] = res[i][1] + res[i-1][1]

print(sum(res[N]))
