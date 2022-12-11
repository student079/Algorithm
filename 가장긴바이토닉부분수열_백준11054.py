from sys import stdin

# 입력
N = int(stdin.readline().rstrip('\n'))
seq = list(map(int, stdin.readline().rstrip('\n').split()))
# 뒤에서 부터 감소해야하니까 리버스한거 생성
re_seq = seq[::-1]

# 증가수열 감소수열 길이 따로 구하기
inres = [1]*N
deres = [1]*N

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            inres[i] = max(inres[i], inres[j] + 1)
        if re_seq[i] > re_seq[j]:
            deres[i] = max(deres[i], deres[j] + 1)
# 감소하는 최대길이 구하고

res = [0]*N
for i in range(N):
    # 같은 인덱스에서 합 저장 후
    res[i] = inres[i] + deres[N-i-1] - 1

# 합이 최대인 값 출력
print(max(res))
