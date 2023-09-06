from collections import deque
import heapq

def solution(jobs):
    
    # 후보들 중에 걸리는 시간이 짧은 거 먼저하면 될듯
    currentTime = 0
    answer = 0
    n = len(jobs)
    
    jobs.sort()
    jobs = deque(jobs)
    heap = []
    
    while True:
        
        # 현재 시간이랑 비교해서 이전인 것들 힙에 넣기
        while jobs and jobs[0][0] <= currentTime:
            start, workTime = jobs.popleft()
            heapq.heappush(heap, (workTime, start))
        
        if heap:
            workTime, start = heapq.heappop(heap)
            currentTime += workTime
            answer += currentTime - start # 소요시간 기록
        else :
            currentTime += 1
        
        if not jobs and not heap:
            break
            
    return answer//n