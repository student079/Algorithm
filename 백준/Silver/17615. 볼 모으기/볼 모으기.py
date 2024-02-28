# N <= 500000

import sys

N = int(sys.stdin.readline())
balls = sys.stdin.readline().rstrip()
cnts = []

# 빨간공
# 오른쪽
cnts.append(balls.rstrip('R').count('R'))
# 왼쪽
cnts.append(balls.lstrip('R').count('R'))

# 파란공
# 오른쪽
cnts.append(balls.rstrip('B').count('B'))
# 왼쪽
cnts.append(balls.lstrip('B').count('B'))

print(min(cnts))