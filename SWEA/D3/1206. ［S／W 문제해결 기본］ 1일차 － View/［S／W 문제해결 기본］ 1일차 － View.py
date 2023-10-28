# 다시 풀어보기

T = 10
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2):
        # 왼쪽 오른쪽 두개까지 비교
        if arr[i] <= arr[i-1] or arr[i] <= arr[i-2] or arr[i] <= arr[i+1] or arr[i] <= arr[i+2]:
            continue

        else:
            m = max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
            res += arr[i] - m
    print("#" + str(t) + " " + str(res))