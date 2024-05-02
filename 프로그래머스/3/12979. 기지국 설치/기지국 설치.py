
# n 2억

def solution(n, stations, w):
    answer = 0

    # w*2+1만큼 커버 가능
    # 빈 부분
    step = 1
    for station in stations:
        if step < station - w:
            dis = station - w - step
            answer += dis // (w*2 + 1)
            if dis % (w*2 + 1) != 0:
                answer+=1
        step = station + w + 1
    
    # 끝부분
    if step <= n:
        dis = n - step + 1
        answer += dis // (w*2 + 1)
        if dis % (w*2 + 1) != 0:
            answer+=1
        
    return answer