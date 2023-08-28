from collections import deque
def solution(priorities, location):
    
    #enumerate, deque 사용해서 index, value 쌍으로 저장
    queue = deque([(i,p) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        currentIndex, currentValue = queue.popleft()
        
        # priority가 있는거보다 작으면 다시 큐에 넣기
        if any(currentValue < priority for _, priority in queue):
            queue.append((currentIndex, currentValue))
        # 크거나 같으면 count 증가시키고 location과 비교해서 같으면 count 리턴
        else:
            count += 1
            if location == currentIndex:
                return count
            
    return count