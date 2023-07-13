def solution(answers):
    a = (1,2,3,4,5)
    b = (2,1,2,3,2,4,2,5)
    c = (3,3,1,1,2,2,4,4,5,5)
    
    aLength = len(a)
    bLength = len(b)
    cLength = len(c)
    
    res = [0,0,0]
    
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == a[idx%aLength]:
            res[0] += 1
        if answer == b[idx%bLength]:
            res[1] += 1
        if answer == c[idx%cLength]:
            res[2] += 1
    
    m = max(res)
    for i in range(3):
        if res[i] == m:
            result.append(i+1)
        
    return result