from sys import stdin

# 입력
N = int(stdin.readline().rstrip('\n'))
seq = list(map(int, stdin.readline().rstrip('\n').split()))

res = [1]*N

for i in range(N):
    for j in range(i):
        if seq[i] < seq[j]:
            # 자기 전에꺼랑 자기 포함해서 한거랑 비교
            res[i] = max(res[i], res[j] + 1)

print(max(res))
