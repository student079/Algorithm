import heapq

def solution(scoville, K):
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return
    
    
    heapq.heapify(scoville)
    time = 0
    
    if scoville[0] >= K:
        return time
    
    # 반복문 돌면서 
    while True:
        time += 1
        sLen = len(scoville)
        # K 이상 안되면 -1
        if sLen < 2:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        heapq.heappush(scoville, a + b*2)
        
        if scoville[0] >= K:
            return time
        