import heapq

def solution(operations):
    
    # heap 두개활용
    
    minHeap = []
    maxHeap = []
    
    for op in operations:
        m, d = op.split(" ")
        d = int(d)
        if m == "I":
            heapq.heappush(minHeap, d)
            heapq.heappush(maxHeap, -d)
        else:
            if d == -1 and minHeap: # 최소값 삭제
                m = heapq.heappop(minHeap)
                maxHeap.remove(-m)
            elif d == 1 and maxHeap : # 최대값 삭제
                m = heapq.heappop(maxHeap)
                minHeap.remove(-m)
    
    if not maxHeap:  # 최대 힙이 비어있다면, 최소 힙도 비어있어야 함
        minHeap = []
    
    return [-maxHeap[0], minHeap[0]] if maxHeap else [0, 0]