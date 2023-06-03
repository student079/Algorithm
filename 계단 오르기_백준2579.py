import sys

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

# dp문제 같음

# 계단 2개 이하는 걍 더하기
if N <= 2:
    print(sum(stairs))
    exit()

# 두개 이상은 점화식 이용
dp = [0] * N
dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]

for i in range(2,N):
    # 지금 계단을 밟는 것을 보장해 주기 위해서 
    # stairs[i]는 꼭 포함
    # 여기서 i가 2일 때 dp[i-3]이 dp[-1]이 되는데 어차피 0이라 상관없다
    # 즉, 지금계단+전계단, 세칸전까지 최대값이랑
    # 두칸전 최대값 + 지금 계단을 비교해서 i가 꼭대기인 계단일때의 최대값을
    # dp에 저장
    dp[i] = max(dp[i-3] + stairs[i - 1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N-1])
