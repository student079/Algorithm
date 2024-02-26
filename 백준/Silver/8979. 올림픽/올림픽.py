# N, K <= 1000

import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

contries = []
for _ in range(N):
    idx, gold, silver, bronze = map(int,sys.stdin.readline().rstrip().split())

    if idx == K:
        tGold, tSilver, tBronze = gold, silver, bronze

    contries.append((idx, gold, silver, bronze))

contries.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(len(contries)):
    idx, gold, silver, bronze = contries[i]

    if (gold, silver, bronze) == (tGold, tSilver, tBronze):
        print(i+1)
        break