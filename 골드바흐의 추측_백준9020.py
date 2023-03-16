import sys

prime = [True] * 10001
i = 2
prime[0] = False
prime[1] = False

while i <= 10000:
    if prime[i] == True:
        j = 2
        while i*j <= 10000:
            prime[i*j] = False
            j += 1
    i += 1

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    n = int(sys.stdin.readline().rstrip('\n'))
    
    a ,b= n//2,n//2
    while a > 0:
        if prime[a] == True and prime[b] == True:
            print(a,b)
            break
        a -= 1
        b +=1

