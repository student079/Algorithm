# A의 연산을 최소로 B 만들기
# 1. A의 아무곳에 문자 하나 삽입
# 2. A의 문자 하나 삭제
# 3. 문자 교체
# 최대 1000글자
# 최대 10000번
# 완전탐색 불가

# dp

import sys

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
aLen = len(A)
bLen = len(B)

# 점화식 구하기
dp = [[-1] * (bLen + 1) for _ in range(aLen + 1)]
for i in range(bLen + 1):
    dp[0][i] = i
for i in range(aLen + 1):
    dp[i][0] = i

for i in range(1, aLen + 1):
    for j in range(1, bLen + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[aLen][bLen])