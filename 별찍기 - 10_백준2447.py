import sys

N = int(sys.stdin.readline().rstrip('\n'))

def printStar(n):
    if n == 3:
        return ["***", "* *", "***"]
    arr = printStar(n//3)
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+" "*(n//3) + i)
    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(printStar(N)))