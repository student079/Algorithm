import sys

num, cutl = map(int, input().split())

lst = sys.stdin.readline()

lst = lst.split(" ")

lst = list(map(int, lst))

lst.sort(reverse=True)

print(lst[cutl-1])
