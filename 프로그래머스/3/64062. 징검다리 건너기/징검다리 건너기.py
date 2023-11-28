def solution(stones, k):
    
    # O(n)으로 해결
    # 0인게 k만큼이면 끝
    # 이분 탐색 같은데
    # left = 최솟값, right = 최댓값
    
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left+right)//2
        
        cnt = 0
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
        
    
    return left