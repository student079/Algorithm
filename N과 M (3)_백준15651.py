import sys, itertools

N, M = map(int,sys.stdin.readline().rstrip('\n').split())


p = itertools.product(range(1,N+1),repeat = M)
for i in p:
    for j in i:
        print(j, end=" ")
    print()