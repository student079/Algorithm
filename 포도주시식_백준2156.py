from sys import stdin

n = int(stdin.readline().rstrip("\n"))
grape = [0]

for _ in range(n):
    grape.append(int(stdin.readline().rstrip('\n')))

dp = [0]
dp.append(grape[1])

if n > 1:
    dp.append(grape[1] + grape[2])

# 경우의 수 로 나누면 점화식 구할 수 있음
# 지금꺼 먹는 경우 -> 전에 꺼 안먹는거 먹는거
# 지금꺼 안먹는 거
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+grape[i - 1]+grape[i], dp[i - 2]+grape[i]))

print(dp[n])
