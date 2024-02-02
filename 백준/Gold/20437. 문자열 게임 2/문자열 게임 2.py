import sys
from collections import defaultdict

T = int(sys.stdin.readline())

def getLength(indexList, K):
    maxLength = 0
    minLength = 10000

    for i in range(len(indexList) - K + 1):
        maxLength = max(maxLength,  indexList[i+K-1] - indexList[i] + 1)
        minLength = min(minLength, indexList[i+K-1] - indexList[i] + 1)
    
    return maxLength, minLength


for _ in range(T):

    maxLength = 0
    minLength = 10000

    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())

    d = defaultdict(list)
    for i, c in enumerate(W):
        d[c].append(i)
    
    for c, indexList in d.items():
        if len(indexList) >= K:
            maxl, minl = getLength(indexList, K)
            maxLength = max(maxl, maxLength)
            minLength = min(minl, minLength)
    
    if minLength == 10000 or maxLength == 0:
        print(-1)
    else:
        print("{} {}".format(minLength, maxLength))

    


