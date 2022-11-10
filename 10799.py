import sys

item = sys.stdin.readline().strip("\n")

stack = []

sum = 0

for i in range(len(item)):
    if item[i] == "(":
        stack.append(item[i])
    else:
        if item[i-1] == "(":
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1

print(sum)
