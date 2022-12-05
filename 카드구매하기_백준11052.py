from sys import stdin

N = int(stdin.readline().rstrip('\n'))
P = list(map(int, stdin.readline().rstrip('\n').split()))
P.insert(0, 0)
res = [0]
for i in range(1, N+1):
    max = 0
    for j in range(i):
        if res[j]+P[i-j] > max:
            max = res[j]+P[i-j]
    res.append(max)

print(res[N])
