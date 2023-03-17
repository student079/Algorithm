import sys

def calendar(M,N,x,y):

    n = y % N
    while(x <= M*N):
        if x % N == n:
            return x
        x += M
    return -1

for _ in range(int(sys.stdin.readline().rstrip('\n'))):
    M, N, x, y = map(int,sys.stdin.readline().rstrip('\n').split())
    print(calendar(M,N,x,y))
"""
M, N, x, y = 10, 12, 3, 9일 때를 살펴보자.
x가 3인 해는 3번째, 13번째, 23번째, 33번째... 해이다.
y가 9인 해는 9번째, 21번째, 33번째... 해이다."""