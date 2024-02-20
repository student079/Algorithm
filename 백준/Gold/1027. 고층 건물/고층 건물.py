import sys

N = int(sys.stdin.readline()) # N 50 
canSees = [0] * N
buildings = list(map(int, sys.stdin.readline().rstrip().split()))
# 50 * 50 * 50 125000

for i in range(N):
    for j in range(i+1, N):

        # 방정식 구하기
        x, y , nx, ny = i, buildings[i], j, buildings[j]
        if y == ny:
            d = 0
            b = y
        else:
            d = (ny - y) / (nx - x)
            b = y - d*x

        # 사이에 건물 있는지 체크
        for k in range(i+1,j):
            if d*k + b <= buildings[k]:
                break
        else:
            canSees[i] += 1
            canSees[j] += 1

print(max(canSees))