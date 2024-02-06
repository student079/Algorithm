# 세로로 N 또는이 가로로 M 보다 큰

import sys
from math import ceil

H, W, N, M = map(int, sys.stdin.readline().split())

row = ceil(W/(M+1))
col = ceil(H/(N+1))

print(row *col)