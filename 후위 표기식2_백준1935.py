from sys import stdin

n = int(stdin.readline().strip("\n"))

exp = stdin.readline().strip("\n")


def compute(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


stack = []
temp = []
for i in range(n):
    temp.append(int(stdin.readline()))

for i in exp:
    if i != '*' and i != '/' and i != '-' and i != '+':
        stack.append(temp[ord(i)-65])
    else:
        b = stack.pop()
        a = stack.pop()
        c = compute(a, b, i)
        stack.append(c)

print("{0:.2f}".format(stack.pop()))
