# dp문제 X의 최솟값을 기억하는 테이블로 X하나씩 늘려가며 계산
import sys

X = int(sys.stdin.readline().rstrip('\n'))

# 최소연산값 기억할 배열 0으로 초기화
dp = [0 for _ in range(X+1)]

# 0,1은 이미 연산횟수가 0 이므로 2부터 시작해서 X까지
for i in range(2, X+1):
    # 이전 수의 최소연산 값 +1 : -1 이 최소 연산일 수 있음
    dp[i] = dp[i-1] + 1

    # 3으로 나누거나 2로 나누었던 값의 최소연산 중 더 작은 값 선택해서 배열 채우기
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

print(dp(X))
