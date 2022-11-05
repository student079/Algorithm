# 재귀는 -1만 있는게 아니다 반환값을 재귀적으로 받을 수 있음

def return_star(num):

    if num == 3:
        return ["***", "* *", "***"]

    arr = return_star(int(num/3))
    Stars = []
    for i in arr:
        Stars.append(i*3)

    for i in arr:
        Stars.append(i+" "*int(num/3)+i)

    for i in arr:
        Stars.append(i*3)

    return Stars


num = int(input())

print("\n".join(return_star(num)))
