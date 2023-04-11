import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int,sys.stdin.readline().split())))

    for i in range(1,n):
        sticker[0][i] = max(sticker[0][i-1],sticker[0][i] + sticker[1][i-1])
        sticker[1][i] = max(sticker[1][i-1],sticker[1][i] + sticker[0][i-1])

    print(max(sticker[0][n-1],sticker[1][n-1]))