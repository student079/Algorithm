def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1]) # 나가는 순으로 정렬해놓고
    camera = -30001 # 카메라 위치
    
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer+=1
    
    return answer