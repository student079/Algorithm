from sys import stdin
N = 9

height = []
for _ in range(N):
    height.append(int(stdin.readline().rstrip()))


for i in range(N - 1):

    for j in range(i+1, N):
        temp = height[:]
        temp[i] = 0
        temp[j] = 0
        if sum(temp) == 100:
            temp.pop(j)
            break
    if sum(temp) == 100:
        temp.pop(i)
        break

for i in sorted(temp):
    print(i)
