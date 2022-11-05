num = int(input())

sums = []

for i in range(1, num+1):

    sum = 0
    temp = i
    while True:
        sum += temp % 10
        temp = temp//10
        if temp < 1:
            sum += i
            break

    if sum == num:
        sums.append(i)

if len(sums) != 0:
    print(min(sums))
else:
    print(0)
