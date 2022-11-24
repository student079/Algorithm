import sys


def how_much(str):
    b = 0
    s = 0
    n = 0
    w = 0
    for i in list(str):
        if i.isalnum():
            if i.isdigit():
                n += 1
            else:
                if i.isupper():
                    b += 1
                else:
                    s += 1
        else:
            w += 1

    print(s, b, n, w)


while True:
    str = sys.stdin.readline().rstrip("\n")
    if not str:
        break
    how_much(str)
