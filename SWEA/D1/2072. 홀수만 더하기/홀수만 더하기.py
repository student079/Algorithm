
T = int(input())

for t in range(1,T+1):
    s = 0
    arr = list(map(int,input().split()))
    for i in arr:
        if i%2 == 1:
            s+=i

    print("#"+str(t)+" "+str(s))