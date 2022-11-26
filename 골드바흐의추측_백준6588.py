import sys

# 소수 빠르게 구하기
def is_prime(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    else:
        i = 2
        while i*i<=num:
            if num%i == 0:
                return False
            i+=1
        return True

while True:
    n = int(sys.stdin.readline().rstrip('\n'))
    if not n:
        break
    i =3
    while i<= int(n/2):
        if is_prime(i) and is_prime(n-i):
            print("{} = {} + {}".format(n,i,n-i))
            break
        i+=2
    else:
        print("Goldbach's conjecture is wrong.")


