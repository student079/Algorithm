import sys

N = int(sys.stdin.readline())
waterList = []
depthList = []
prevY = -1
for _ in range(N):
    x, y = map(int ,sys.stdin.readline().rstrip().split())
    if y == prevY:
        for i in range(prevX, x):
            waterList.append(y)
            depthList.append(y)
    prevX , prevY = x, y
K = int(sys.stdin.readline())
holeList = []
for _ in range(K):
    a, b,c,_ = map(int ,sys.stdin.readline().rstrip().split())
    # y, sx, ex
    holeList.append((b, a,c))

for y, sx, ex in holeList:
    # 범위 해당하는 곳 다 가지고 있는 water 0
    for i in range(sx, ex):
        waterList[i] = 0
    
    # 왼쪽 오른쪽 구멍 깊이비교 후 물 빼기
    # 왼쪽
    minY = y
    for i in range(sx):
        minY = min(minY, depthList[i])
        waterList[i] = min(waterList[i], depthList[i] -minY)

    # 오른쪽
    minY = y
    for i in range(ex, len(waterList)):
        minY = min(minY, depthList[i])
        waterList[i] = min(depthList[i] - minY, waterList[i])

print(sum(waterList))