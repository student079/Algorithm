from collections import deque

def solution(queue1, queue2):
    
    answer = 0
    
    # 두 큐 원소들 합이 같도록 작업 최소로
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1+sum2) % 2 == 1:
        return -1
    
    while True:
        
        if sum1 == sum2:
            return answer
        
        answer += 1
        
        if answer == 4 * len(queue1):
            return -1
        
        if sum1 > sum2:
            n = queue1.popleft()
            queue2.append(n)
            sum1 -= n
            sum2 += n
        else :
            n = queue2.popleft()
            queue1.append(n)
            sum1 += n
            sum2 -= n
        
        