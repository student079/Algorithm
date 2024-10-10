from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    
    while q:
        answer += 1
        weight = q.pop()
        if q and weight + q[0] <= limit:
            q.popleft()
    
    return answer