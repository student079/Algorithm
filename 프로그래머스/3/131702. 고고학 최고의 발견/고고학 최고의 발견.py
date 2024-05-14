# 2 ≤ clockHands의 길이 ≤ 8
# 64개
# 첫번째 row 회전시키는 모든 경우의 수
# 둘째 row는 그리디 하게

from copy import deepcopy
from itertools import product

def solution(clockHands):
    answer = float('inf')
    length = len(clockHands)
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    
    def rotate(x, y, cnt, clock):
        # 자신 + 인접한 것들
        clock[x][y] = (clock[x][y] + cnt) % 4
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < length and 0 <= ny < length:
                clock[nx][ny] = (clock[nx][ny] + cnt) % 4
    
    # 첫번째 줄 돌리는 모든 경우
    for case in product(range(4), repeat=length):
        clock = deepcopy(clockHands)
        
        for j in range(length):
            rotate(0, j, case[j], clock)
        
        # 첫째줄 돌리는 cnt
        cnt = sum(case)
        
        # 두번째줄부터는 보면서
        for i in range(1, length):
            for j in range(length):
                if clock[i-1][j] != 0:
                    t = 4 - clock[i-1][j]
                    rotate(i, j, t, clock)
                    cnt += t
        
        if sum(clock[length-1]) == 0:
            answer = min(answer, cnt)
        
    return answer