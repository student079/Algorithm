from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque()  # 현재 다리 위의 트럭
    time = 0
    total_weight = 0
    last_entered_time = 0
    
    # while문 돌면서 count 증가
    while truck_weights or on_bridge:
        time += 1
        
        # 나갈 트럭
        if on_bridge and time - on_bridge[0][1] >= bridge_length:
            truck, entered_time = on_bridge.popleft()
            total_weight -= truck
        
        # length랑 sum체크해서 더들어갈 수 있으면
        if truck_weights and total_weight + truck_weights[0] <= weight and len(on_bridge) + 1 <= bridge_length:
            truck = truck_weights.popleft()
            total_weight += truck
            on_bridge.append((truck, time)) # 튜플 형태로 넣기
    
    return time
