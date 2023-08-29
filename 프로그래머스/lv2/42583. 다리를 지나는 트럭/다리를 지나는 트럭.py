from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    stack = deque()
    truck_weights = deque(truck_weights)
    count = 0
    
    # while문 돌면서 count 증가
    while truck_weights or stack:
        count+=1 # time
        
        # 나갈 트럭
        if any(count - i[1] >= bridge_length for i in stack):
            stack.popleft()
        
        # length랑 sum체크해서 더들어갈 수 있으면
        if truck_weights and sum(i[0] for i in stack)+truck_weights[0] <= weight and\
        len(stack) + 1 <= bridge_length:
            # 튜플 형태로 넣기
            stack.append((truck_weights.popleft(), count))
        
            
    return count