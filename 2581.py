num1 = int(input())
num2 = int(input())

lst_no = range(num1, num2+1)
result_list = []
result = 0
for i in lst_no:
    j = 2
    if i == 2:
        result_list.append(2)
        continue
    while i != j:
        if i == 1:
            break
        if i % j == 0:
            break
        if i % j != 0 and i-1 == j:
            result_list.append(i)
        j += 1

for i in result_list:
    result += i

if len(result_list) == 0:
    print("-1")
else:
    print(result)
    print(int(min(result_list)))
