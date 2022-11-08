import sys


def VPS(str):
    lst = []
    for i in str:
        if i == "(":
            lst.append(i)
        elif i == ")" and "(" in lst:
            del lst[-1]
        elif i == ")" and "(" not in lst:
            return "NO"
        else:
            continue

    if "(" in lst:
        return "NO"
    else:
        return "YES"


item = int(sys.stdin.readline())

for _ in range(item):
    str = sys.stdin.readline().strip("\n")
    print(VPS(str))
