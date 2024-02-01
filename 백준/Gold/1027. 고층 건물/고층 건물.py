import sys
from collections import defaultdict

# 좌표로 해보자

# 50 * 50
# 딕셔너리로 저장 
N = int(sys.stdin.readline())
buildings = list(map(int,sys.stdin.readline().split()))
d = defaultdict(int)

for i in range(N):

    for idx, h in enumerate(buildings):
        if idx <= i:
            continue

        # 높이 같은거면 둘다 추가해줘야함
        if buildings[i] != h:
            dxdy = (h - buildings[i])/(idx - i)
            k = h - dxdy * idx
        else:
            dxdy = 0
            k = h
        
        check = True
        for x, y in enumerate(buildings):
            if not (i < x < idx):
                continue
            if dxdy * x + k <=  y:
                check = False
                break
        
        if check:
            d[idx] += 1
            d[i] += 1
           
if len(d) == 0:
    print(0)
else:
    print(max(d.values()))


