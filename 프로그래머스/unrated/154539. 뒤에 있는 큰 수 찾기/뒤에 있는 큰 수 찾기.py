def solution(numbers):
    answer = []
    
    stack = []
    for i in range(len(numbers)):
        num = numbers.pop()
        
        while stack:
            if num >= stack[-1]:
                stack.pop()
            else :
                answer.append(stack[-1])
                stack.append(num)
                break
        
        if not stack:
            answer.append(-1)
            stack.append(num)
            continue
            
    answer.reverse()
    
    return answer