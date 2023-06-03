import sys

n = int(sys.stdin.readline())
seq = tuple(int(sys.stdin.readline()) for _ in range(n))

# 스택 만들고
# 못만드는 거는 스택에 없고 idx가 그 수보다 크면 못만든다
stack = []
idx = 1
res = ""
for i in seq:
    if i < idx and i not in stack:
        print("NO")
        exit()

    # idx가 i 보다 작으면 푸쉬
    while idx <= i:
        stack.append(idx)
        idx +=1
        res+="+"

    # stack에 값이 있고 top이 i가 될때까지 pop
    while stack and stack[-1] >= i:
        stack.pop()
        res+="-"

for i in list(res):
    print(i)

