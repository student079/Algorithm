import sys

item = int(sys.stdin.readline())

stack = []
result = []
flag = 0
cur = 1
for i in range(item):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = 1

if flag == 0:
    for i in result:
        print(i)
else:
    print("NO")
