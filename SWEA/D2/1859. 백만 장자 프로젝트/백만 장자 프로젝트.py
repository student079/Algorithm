# 다시 풀어보기

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    res = 0
    m = 0

    for i in arr[::-1]:
        if i > m:
            m = i
        else :
            res += m-i
    print("#" + str(t) + " " + str(res))