from sys import stdin

N = int(stdin.readline().rstrip('\n'))
P = list(map(int, stdin.readline().rstrip('\n').split()))
P.insert(0, 0)
res = [0]
for i in range(1, N+1):
    min = 10000
    for j in range(i):
        if res[j]+P[i-j] < min:
            min = res[j]+P[i-j]
    res.append(min)

print(res[N])
