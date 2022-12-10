from sys import stdin

n = int(stdin.readline().rstrip('\n'))
tr = []
for _ in range(n):
    tr.append(list(map(int, stdin.readline().rstrip('\n').split())))

# 주체가 더해질 숫자
# 자기가 될 경우의 합들을 자기자리에 저장해주는 것
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽가장자리, 오른쪽 가장자리면 무조건 정해짐
        # 그 외에는 왼쪽위랑 오른쪽위 중에 최댓값 더해
        if j == 0:
            tr[i][j] += tr[i-1][j]
        elif i == j:
            tr[i][j] += tr[i-1][j-1]
        else:
            tr[i][j] += max(tr[i-1][j-1], tr[i-1][j])

print(max(tr[n-1]))
