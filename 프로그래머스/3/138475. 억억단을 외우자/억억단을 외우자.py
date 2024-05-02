# e 오백만
# 약수로 판단

def solution(e, starts):
    answer = []
    cnts = [0] * (e+1)
    
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            cnts[i*j]+=2
            
    maxCnt = 0
    for i in range(e,0,-1):
        if maxCnt <= cnts[i]:
            maxCnt = cnts[i]
            cnts[i] = i
        else:
            cnts[i] = cnts[i+1]
    
    for s in starts:
        answer.append(cnts[s])
    
    return answer