import sys

item = int(sys.stdin.readline())


def reverse(str):
    for i in str:
        print("{}".format(i[::-1]), end=" ")


for _ in range(item):
    str = sys.stdin.readline().split()
    reverse(str)
    print()
