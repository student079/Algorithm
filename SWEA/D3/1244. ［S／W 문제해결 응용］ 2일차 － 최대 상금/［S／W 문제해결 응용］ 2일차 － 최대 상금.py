# 다시 풀어보기

def dfs(cnt, idx):
    global res

    if cnt == int(e_cnt):
        res = max(res, int("".join(map(str,arr))))
        return

    for i in range(idx, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                dfs(cnt + 1, i)
                arr[i], arr[j] = arr[j], arr[i]

    if res == 0 and cnt < int(e_cnt):
        if (int(e_cnt) - cnt)%2:
            arr[-1], arr[-2] = arr[-2], arr[-1]
        dfs(int(e_cnt), idx)
    return

T = int(input())
for t in range(1, T+1):
    arr, e_cnt = input().split(' ')
    arr = list(map(int, arr))
    res = 0
    dfs(0, 0)
    print(f'#{t} {res}')


