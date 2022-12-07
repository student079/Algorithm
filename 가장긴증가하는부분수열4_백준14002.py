from sys import stdin

N = int(stdin.readline().rstrip('\n'))
seq = list(map(int, stdin.readline().rstrip('\n').split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

res = []  # 정답수열 입력할 배열선언
order = max(dp)  # max(dp) 값을 저장
for i in range(N - 1, -1, -1):
    if dp[i] == order:  # 만약 dp[i] 값이 order값과 같다면
        res.append(seq[i])  # 해당 input_array[i]값을 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

res.reverse()  # 큰수부터 작은수로 뽑았기 때문에
print(*res)  # 정답수열 출력
