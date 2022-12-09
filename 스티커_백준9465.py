from sys import stdin

T = int(stdin.readline().rstrip('\n'))
arr = [[0]*100000]*2
for _ in range(T):
    n = int(stdin.readline().rstrip('\n'))

    arr[0] = list(map(int, stdin.readline().rstrip('\n').split()))
    arr[1] = list(map(int, stdin.readline().rstrip('\n').split()))

    if n != 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
    # 주체가 더해질 숫자다
    # 더해질 숫자기준으로 왼쪽 대각, 그 대각의 한칸 왼쪽 중 큰거 선택하면 됨
    for i in range(2, n):
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    print(max(arr[0][n-1], arr[1][n-1]))
