import sys

item = int(sys.stdin.readline())

lst = []


def push(lst, num):
    lst.append(num)


def pop(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst.pop(0))


def size(lst):
    print(len(lst))


def empty(lst):
    if len(lst) == 0:
        print(1)
    else:
        print(0)


def front(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[0])


def back(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])


for _ in range(item):
    command = sys.stdin.readline().strip("\n")
    if command[0:4] == "push":
        push(lst, int(command[5:]))
    elif command == "pop":
        pop(lst)
    elif command == "size":
        size(lst)
    elif command == "empty":
        empty(lst)
    elif command == "front":
        front(lst)
    elif command == "back":
        back(lst)
