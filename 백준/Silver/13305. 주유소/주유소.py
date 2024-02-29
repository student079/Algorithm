# 그리디로 될것같은데

import sys

N = int(sys.stdin.readline())
distances = list(map(int,sys.stdin.readline().rstrip().split()))
oils = list(map(int,sys.stdin.readline().rstrip().split()))

res = 0
oilMin = oils[0]
for i in range(N-1):
    if oils[i] < oilMin:
        oilMin = oils[i]
    res += oilMin * distances[i]

print(res)