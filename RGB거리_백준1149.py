from sys import stdin

N = int(stdin.readline().rstrip('\n'))
house = []
for _ in range(N):
    house.append(list(map(int, stdin.readline().rstrip('\n').split())))

# i가 각각 RGB일 때 전에 것들의 경우들의 최솟값+ i가 RGB일 때 저장
for i in range(1, N):
    house[i][0] = min(house[i - 1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i-1][1]) + house[i][2]
    print(house)

print(min(house[N-1][0], house[N-1][1], house[N-1][2]))
