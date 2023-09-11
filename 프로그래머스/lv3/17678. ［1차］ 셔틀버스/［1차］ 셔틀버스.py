def solution(n, t, m, timetable):
    
    # 구현?
    
    answer = 0
    
    # 시간계산 편하게 정수로
    timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    timetable.sort()
    
    # 버스 도착 시각 리스트
    bus_time = [9*60 + t*i for i in range(n)]
    timetable_len = len(timetable)
    
    idx = 0
    for time in bus_time:
        cnt = 0 # 버스에 탄 사람
        while cnt < m and idx < timetable_len and timetable[idx] <= time:
            cnt += 1
            idx += 1
        if cnt < m : # 자리 남음
            answer = time
        else:   # 자리 없으면 마지막사람보다 1분 일찍
            answer = timetable[idx - 1] - 1
            
    
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)