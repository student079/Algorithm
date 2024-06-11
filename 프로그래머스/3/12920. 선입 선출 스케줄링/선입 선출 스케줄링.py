# 이분 탐색

def solution(n, cores):
    lenCores = len(cores)
    
    if n < lenCores:
        return n
    
    n -= lenCores
    left = 1
    right = max(cores) * n
    
    while left < right:
        mid = (left + right)// 2
        capacities = 0
        
        for c in cores:
            capacities += mid // c
        
        if capacities >= n:
            right = mid
        else :
            left = mid + 1
    
    for c in cores:
        n -= (right-1) // c
    
    for i in range(lenCores):
        if right % cores[i] == 0:
            n-= 1
            if n == 0:
                return i + 1