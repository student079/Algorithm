# N, K <= 1000

import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

contries = []
for _ in range(N):
    contries.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

contries.sort(key = lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for i in range(1,len(contries)):
    idx, gold, silver, bronze = contries[i]
    preIdx, preGold, preSilver, preBronze = contries[i-1]

    rank += 1
    if (gold, silver, bronze) == (preGold, preSilver, preBronze):
        rank -= 1
    
    if idx == K:
        print(rank)
        break

    