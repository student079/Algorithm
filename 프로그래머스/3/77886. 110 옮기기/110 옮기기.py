# 다시 풀어보기

def solution(s):
    answer = []
    
    for x in s:
        stack = []
        cnt110 = 0
        for i in x:
            if i == '0' and len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1':
                stack.pop()
                stack.pop()
                cnt110 += 1
            else:
                stack.append(i)
        
        
        stack = "".join(map(str,stack))
        i = stack.find("111")
        # 111 없으면 가장 뒤의 0 뒤에 110 삽입
        if i == -1:
            idx = stack.rfind('0')
            answer.append(stack[:idx+1] + "110"*cnt110 + stack[idx+1:])
        # 잇으면 111 앞에 110 삽입
        else:
            answer.append(stack[:i] + "110" * cnt110 + stack[i:])
        
    return answer