def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


def re_two_prime(a, b):
    while True:
        if isPrime(a) and isPrime(b):
            return a, b
        else:
            a -= 1
            b += 1


item = int(input())

i = 0
while i < item:
    i += 1
    num = int(input())

    a, b = int(num/2), int(num/2)

    result_a, result_b = re_two_prime(a, b)
    print(result_a, result_b)
