# 플레이어 N명
# 각각 M장 카드
# N, M ~ 100
# 자신이 가진 카드 중 가장 큰 가드로 비교
# 가장 큰 수를 가진 플레이어가 1점 획득
# 턴 마다 카드 사용하고 버리기

# 정렬한후에 하나씩 빼기

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

# 정렬 log m 
# * n 명
scores = [0] * (N+1)

cards = [[]]

for _ in range(N):
    cards.append(sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True))

# M 번의 경기 후
for round in range(M):
    temp = []
    for i in range(1, N+1):
        temp.append(cards[i][round])
    cardMax = max(temp)
    for i in range(1, N+1):
        if cards[i][round] == cardMax:
            scores[i] += 1

scoreMax = max(scores[1:])

res = []
for i in range(1, N+1):
    if scores[i] == scoreMax:
        res.append(i)
    
print(*res)