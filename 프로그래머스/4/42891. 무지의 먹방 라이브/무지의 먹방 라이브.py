# 원형큐
# 200,000
# 100,000,000의 자연수

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    L = len(food_times)
    sortedFood = sorted(enumerate(food_times), key=lambda x:x[1])
    
    idx = 0
    s = 0
    pre = 0
    while s + (sortedFood[idx][1] - pre) * L < k : 
        s += (sortedFood[idx][1] - pre) * L
        pre = sortedFood[idx][1]
        L -= 1
        idx += 1
        
    res = sorted(sortedFood[idx:])
    
    return res[(k-s)%L][0] + 1