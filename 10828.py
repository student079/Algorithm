import sys

item = int(sys.stdin.readline())


def push(x, lst):
    lst.append(x)


def pop(lst):
    if len(lst) == 0:
        return -1
    else:
        idx = len(lst)-1
        num = lst[idx]
        del lst[idx]
        return num


def size(lst):
    return len(lst)


def empty(lst):
    if len(lst) == 0:
        return 1
    else:
        return 0


def top(lst):
    if len(lst) == 0:
        return -1
    else:
        return lst[len(lst)-1]


lst = []

for _ in range(item):
    com = sys.stdin.readline().strip("\n")
    if "push" in com:
        push(int(com[5:]), lst)
    elif com == "pop":
        print(pop(lst))
    elif com == "size":
        print(size(lst))
    elif com == "empty":
        print(empty(lst))
    elif com == "top":
        print(top(lst))
