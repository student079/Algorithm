from sys import stdin

A, B = map(int, stdin.readline().rstrip('\n').split())
m = int(stdin.readline().rstrip('\n'))
num = stdin.readline().rstrip('\n').split()
res = []
temp = 0
data = 1
for _ in range(m):
    temp += int(num.pop()) * data
    data *= A

while temp >= B:
    res.insert(0, temp % B)
    temp //= B

res.insert(0, temp)

for i in res:
    print(i, end=" ")
