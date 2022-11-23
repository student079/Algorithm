# 후위표기식 변환빙밥
from sys import stdin

bef = stdin.readline().strip('\n')
stack = []
aft = ""
for i in bef:
    # 피연산자면 그냥 출력
    if i.isalpha():
        aft += i
    else:
        if i == '(':
            stack.append(i)
        # 우선순위 따라서 결정
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                aft += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                aft += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                aft += stack.pop()
            stack.pop()
# 남은것들 출력
while stack:
    aft += stack.pop()
print(aft)
