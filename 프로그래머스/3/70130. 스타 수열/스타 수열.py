# 1 <= a <= 500,000

from collections import Counter

def solution(a):
    answer = -1
    counter = Counter(a)
    
    for i in counter.keys():
        if counter[i] * 2 <= answer :
            continue
            
        cnt = 0
        idx = 0
        while idx + 1 < len(a):
        
            if a[idx] != a[idx+1] and (a[idx] == i or a[idx+1] == i):
                cnt += 2
                idx+=1
            idx += 1
        answer = max(cnt, answer)
            
    
    return answer