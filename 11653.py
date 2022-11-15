num = int(input())
i = 2
while num != 1:
    if num % i == 0:
        num /= i
        print(i)
        i = 2
    else:
        i += 1
