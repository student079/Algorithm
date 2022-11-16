# 스택으로 시간복잡도 최소화

import sys

item = int(sys.stdin.readline())

lst = map(int, sys.stdin.readline().strip("\n").split())

lst = list(lst)
result = [-1]*item
stack = []

for i in range(item):
    while stack and stack[-1][0] < lst[i]:
        result[stack.pop()[1]] = lst[i]

    stack.append([lst[i], i])

for i in result:
    print(i, end=" ")
