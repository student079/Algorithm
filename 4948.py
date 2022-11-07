#  속도향상위해 소수 구해놓고 뽑아쓰기

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


nums = []

for i in range(2, 123456*2):
    if isPrime(i):
        nums.append(i)
    else:
        continue

while True:
    num = int(input())

    if num == 0:
        break

    result = 0
    for i in nums:
        if i <= num:
            continue
        elif num < i and i <= num*2:
            result += 1
        else:
            break

    print(result)
