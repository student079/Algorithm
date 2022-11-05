num = int(input())

lst = []

for _ in range(num):
    t = int(input())
    lst.append(t)

lst.sort()

for i in lst:
    print(i)
