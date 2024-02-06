import sys

while True:
    arr = sorted(list(map(int, sys.stdin.readline().split())))

    a, b ,c = arr

    if a == 0 and b == 0 and c == 0:
        exit(0)

    if c >= a + b:
        print("Invalid")
    elif a == b and b == c and c == a:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
    