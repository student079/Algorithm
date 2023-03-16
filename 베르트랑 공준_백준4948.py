#범위가 주어지고 소수 구할때는
#에라토스테네스의 체 쓰는게 빠르다
import sys

prime = [True]*246913

i = 2
prime[0] = False
prime[1] = False
#에라토스테네스의 체:
#2는 소수이고 2의 배수들은 다 합성수
#3은 소수이고 3의 배수들은 다 합성수
#4는 이미 합성수(2의 배수) -> 넘어감
#...
while i < 246913:
    if prime[i] == True:
        j = 2
        while i*j < 246913:
            prime[i*j] = False
            j+=1
    i+=1

problem = []
while True:
    n = int(sys.stdin.readline().rstrip('\n'))
    if n == 0:
        break
    problem.append(n)

for i in problem:
    s = 0
    for j in range(i+1, 2*i+1):
        if prime[j] == True:
            s += 1
    print(s)