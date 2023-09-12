def solution(n, s):
    if s < n:
        return [-1]
    
    num = s // n
    
    answer = [num] * n
    
    for idx in range(s%n):
        answer[n -idx -1] += 1
        
    return answer