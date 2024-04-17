# 인접한 카드
# N 1 ~ 1000
# 레벨 높은 카드로 해야함


import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
maxCard = max(cards)

idx = cards.index(maxCard)
answer = 0

left = cards[:idx]
answer += cards[idx] * len(left) + sum(left)
right = cards[idx+1:]
answer += cards[idx] * len(right) + sum(right)

print(answer)