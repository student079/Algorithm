import sys

number = [0] * 10

a = int(sys.stdin.readline().rstrip("\n"))
b = int(sys.stdin.readline().rstrip("\n"))
c = int(sys.stdin.readline().rstrip("\n"))

for i in str(a*b*c):
    number[int(i)] += 1

for i in number:
    print(i)