import sys

N = int(sys.stdin.readline())
# index = 열, value = 행
# col[2] = 3 -> 2열 3행 -> [2,3]
col = [0] * N
answer = 0

# dfs사용 + 백트래킹으로 간단하게
# 퀸 대각선 + 십자가 모양 다가능
# 대각선 x좌표의 차이랑 y좌표 차이가 동일하면 같은 대각선
# col로 나눠서 열은 체크 안해도댐

def check(y):
    for i in range(y):
        # 대각선 십자가 체크
        if col[y] == col[i] or abs(col[y] - col[i]) == y-i:
            return False
    return True

def dfs(y):
    global answer

    if y == N:
        answer+=1
        return 

    for i in range(N):
        # y열에 i행에 퀸
        col[y] =i
        if check(y):
            # 다음 열 체크
            dfs(y+1)

dfs(0)
print(answer)