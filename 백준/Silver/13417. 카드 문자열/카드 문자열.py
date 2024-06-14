# 왼쪽 또는 오른쪽
# 2**1000 완탐 불가
# 가장왼쪽보다 빠른거만 왼쪽으로

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(sys.stdin.readline().rstrip().split())
    
    mine = deque([cards[0]])
    for card in cards[1:]:
        if card <= mine[0]:
            mine.appendleft(card)
        else:
            mine.append(card)
    
    print("".join(mine))
