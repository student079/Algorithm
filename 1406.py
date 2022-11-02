# 스택 두개 활용해서 마지막엔 뒤집기
# insert가 O(n)이라 느림
# 인덱스 접근 보다 스택접근

import sys
from unittest.util import strclass

str = sys.stdin.readline().strip("\n")
str2 = []
item = int(sys.stdin.readline())

str = list(str)


def edit(command):
    global curse
    if command == "L":
        if str:
            str2.append(str.pop())
    elif command == "D":
        if str2:
            str.append(str2.pop())
    elif command == "B":
        if str:
            str.pop()
    elif command[0] == "P":
        str.append(command[2])


for _ in range(item):
    edit(sys.stdin.readline().strip("\n"))

str.extend(reversed(str2))

for i in str:
    print(i, end="")
