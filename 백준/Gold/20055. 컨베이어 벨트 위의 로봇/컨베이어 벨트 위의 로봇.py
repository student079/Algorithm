# 구현

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
durabilities = list(map(int,sys.stdin.readline().split()))

# 리스트에 로봇 있는지 TRUE, FALSE 같이 저장
durabilities = deque([[d, False] for d in durabilities])

step = 0
up = 0
down = N - 1

while True:
    step += 1

    # 벨트 회전
    durabilities.rotate(1)

    # 로봇 내리기
    durabilities[down][1] = False

    # 로봇 이동
    for i in range(N-2,-1,-1):
        d, exist = durabilities[i]

        if exist:
            if durabilities[i+1][1] == False \
                and durabilities[i+1][0] > 0:
                durabilities[i+1][1] = True
                durabilities[i][1] = False
                durabilities[i+1][0] -= 1
    
    # 로봇 내리기
    durabilities[down][1] = False

    # 로봇 올리기
    if durabilities[up][0] > 0:
        durabilities[up][1] = True
        durabilities[up][0] -= 1

    if sum(1 for d,_ in durabilities if d == 0) >= K:
        print(step)
        break

    
    


