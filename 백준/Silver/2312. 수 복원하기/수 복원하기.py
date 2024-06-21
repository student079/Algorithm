import sys

input = sys.stdin.readline

def find(num):
    i = 2
    cnt = 0
    res = []
    while num >= i:
        if num % i == 0:
            cnt+=1
            num//=i
        else:
            if cnt > 0:
                res.append((i,cnt))
                cnt = 0
            i+=1
    if cnt:
        res.append((i,cnt))
        cnt = 0
    return res

T = int(input())
for _ in range(T):
    for a, b in find(int(input())):
        print(a ,b)
