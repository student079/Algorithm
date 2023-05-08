import sys

# input
n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

# value update
# most left node = from tri[i-1][j]
# most right node = from tri[i-1][j-1]
# else max(tri[i-1][j-1], tri[i-1][j])
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))
