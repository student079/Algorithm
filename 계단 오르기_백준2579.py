#dp 

import sys

N = int(sys.stdin.readline().strip('\n'))

stairs = [0]*301
dp = [0] * 301
#계단 개수 최대 300개
for i in range(N):
    stairs[i] = int(sys.stdin.readline().strip('\n'))

#dp는 최댓값
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,N):
    #세번연속인지 확인하는 거 말고그전, 그전전에 한칸 띄워서 생각
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
print(dp[N-1])