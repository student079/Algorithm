# 직선 판별
# 3개의 점
# 그냥 기울기 같은지 구하기
# x, y 1 ~ 1000

import sys

points = []
for _ in range(3):
    points.append((list(map(int,sys.stdin.readline().rstrip().split()))))

points.sort()

# 두번째가 하나 셋 사이에 끼어있는지

x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]

if (x3 - x1) == 0:
    if x2 == x3:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
elif (y3- y1) == 0:
    if y2 == y3:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")
else:
    d = (y3 - y1) / (x3 - x1)
    y0 = y3 - d*x3
    if d*x2 + y0 == y2:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")