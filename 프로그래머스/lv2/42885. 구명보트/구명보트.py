from collections import deque
def solution(people, limit):
    
    cnt = 0
    people.sort()
    people = deque(people)
    
    cLimit = limit
    while people:
        cnt += 1
        cLimit -= people.pop()
        if people and cLimit >= people[0]:
            people.popleft()
        cLimit = limit
    
    return cnt