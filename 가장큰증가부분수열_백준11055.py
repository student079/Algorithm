from sys import stdin

N = int(stdin.readline().rstrip('\n'))
seq = list(map(int, stdin.readline().rstrip('\n').split()))

dp = [1] * N
dp[0] = seq[0]
for i in range(N):
    for j in range(i):
        # 증가하는 부분이면
        if seq[i] > seq[j]:
            # 원래꺼랑 전에꺼 + 이번꺼 의 최댓값 저장
            dp[i] = max(dp[i], dp[j] + seq[i])
            # 증가하는거 아니면
        else:
            # 원래꺼랑 지금꺼 중에 최댓값 저장
            dp[i] = max(dp[i], seq[i])

print(max(dp))
