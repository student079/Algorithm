import sys

n, m = map(int,sys.stdin.readline().split())

def count(num, divnum):
    count = 0

#팩토리얼에 divnum이 곱해진 개수는 
#divnum의 배수의 개수 + divnum^2의 배수의 개수 + ... 이므로
    if num < divnum:
        return 0
    while num >= divnum:
        count += num//divnum
        num//=divnum
    return count

two = count(n,2) - count(n-m,2) - count(m,2)
five = count(n,5) - count(n-m,5) - count(m,5)

print(min(two,five))

