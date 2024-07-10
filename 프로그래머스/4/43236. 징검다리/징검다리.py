def solution(distance, rocks, n):
    answer = 0
    
    # 이분탐색
    
    rocks.sort()
    left = 0
    right = distance
    while left <= right:
        mid = (left + right)//2
        
        # mid는 거리의 최솟값
        #mid보다 작은거 빼기
        x = 0
        cnt = 0
        for r in rocks:
            if r - x < mid:
                cnt+=1
            else:
                x = r
        if distance - x < mid:
            cnt+=1
        
        if cnt > n:
            right = mid-1
        else:
            left = mid + 1
    
    
    return right