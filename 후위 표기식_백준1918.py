import sys

bef = list(sys.stdin.readline().rstrip('\n'))

# 문자열 받은거 리스트로 바꾸고
# 반복문 돌면서 연산자나 괄호 아닌 것들은 결과문자열에 넣고
# 연산자는 스택에 넣고 */연산자 다음에 +-나오면 pop
# -> +-나오면 pop해버리기
# 연산자는 스택에 넣고 닫는 괄호 만나면 바로 여는 괄호 나올때까지 pop

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
