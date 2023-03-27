import sys

arr = sys.stdin.readline().rstrip('\n')
stack =[]
res = 0

for i in range(len(arr)):
    # (를 만나면 스택에 넣는다
    if arr[i] == "(":
        stack.append("(")
    else:
        # )를 만나면 전에 (가 나왔다면 레이저니까 스택에서 (하나 꺼내고
        # stack에 쌓인 (개수 만큼 res에 더해주기
        if arr[i-1] == "(":
            stack.pop()
            res += len(stack)
        # 전에 )가 나왔으면 레이저가 아니니까 쇠막대기 끄트머리이므로
        #res에 +1해주기
        else:
            stack.pop()
            res += 1

print(res)