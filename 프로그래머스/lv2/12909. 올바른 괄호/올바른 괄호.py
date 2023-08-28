def solution(s):
    
    # 스택 활용
    
    stack = []
    
    # '('이면 무작정 스택에 넣고
    # ')'이면 스택 비어있는지 확인하고 있으면 pop
    # 비어있으면 바르게 짝지어지지 않음 return False
    # 복잡도 O(n)
    for i in s:
        if i == '(':
            stack.append(i)
        else :
            if stack:
                stack.pop()
            else:
                return False

    # 스택에 짝지어지지 않은 '('확인
    if stack:
        return False
    
    return True