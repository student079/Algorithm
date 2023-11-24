def solution(survey, choices):
    
    # 딕셔너리에 넣고 점수 더하기
    
    d = {'R':0, 'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        a,b = list(survey[i])
        
        choice = choices[i]-4
        if choice > 0:
            d[b] += choice
        elif choice < 0:
            d[a] += choice*-1
    
    
    answer = ''
    
    d = list(d.items())
    for i in range(0,8,2):
        answer += d[i][0] if d[i][1] >= d[i+1][1] else d[i+1][0]
    return answer