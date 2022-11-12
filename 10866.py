# 덱: 스택,큐 합친거
#  앞뒤로 가능

import sys

item = int(sys.stdin.readline())

lst = []

for _ in range(item):
    command = sys.stdin.readline().strip("\n")
    if command[:10] == "push_front":
        lst.insert(0, int(command[10:]))
    elif command[:9] == "push_back":
        lst.append(int(command[9:]))
    elif command == "pop_front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(0))
    elif command == "pop_back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif command == "size":
        print(len(lst))
    elif command == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])

    elif command == "back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
