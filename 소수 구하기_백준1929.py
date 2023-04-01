import sys

M, N = map(int,sys.stdin.readline().split())

prime_matrix = [True] * (N+1)
prime_matrix[0] = False
prime_matrix[1] = False

for i in range(N+1):
    if prime_matrix[i]:
        j = 2
        while i*j <= N:
            prime_matrix[i*j] = False
            j+=1

    if M <= i <= N and prime_matrix[i]:
        print(i)