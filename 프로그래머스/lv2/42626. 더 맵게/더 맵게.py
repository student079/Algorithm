import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    time = 0
    # 반복문 돌면서 
    while scoville[0] < K:
        # K 이상 안되면 -1
        if len(scoville) <= 1:
            return -1
        
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)

        new_scoville = first_min + (second_min * 2)
        heapq.heappush(scoville, new_scoville)

        time += 1

    return time