import sys
from copy import deepcopy

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

# 상하좌우의 네가지가 5번 4^5
# dfs로 가능해
# 위쪽으로 밀면 위에서 두번째부터 그위랑 비교해서 합치기
# 보드 deepcopy하기
# target 변수를 만들어서 합쳐지면 다른것을 가리키게끔 해서
# 중복 방지

def up(board):
    for j in range(N):
        # 열 하나씩 확인
        target = 0
        for i in range(1,N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                # 타켓이 0 일때
                if board[target][j] == 0:
                    board[target][j] = temp
                # 타겟이 현재 값과 같을 때 제곱하고 타겟 한칸 내리기
                elif board[target][j] == temp:
                    board[target][j] = temp*2
                    target+=1
                # 그 외라면 타겟 한칸내리고 그자리에 현재 값 넣기
                else:
                    target+=1
                    board[target][j] = temp
    return board

def down(board):
    for j in range(N):
        # 열 하나씩 확인
        target = N-1
        for i in range(N-2,-1,-1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                # 타켓이 0 일때
                if board[target][j] == 0:
                    board[target][j] = temp
                # 타겟이 현재 값과 같을 때 제곱하고 타겟 한칸 올리기
                elif board[target][j] == temp:
                    board[target][j] = temp*2
                    target-=1
                # 그 외라면 타겟 한칸올리고 그자리에 현재 값 넣기
                else:
                    target-=1
                    board[target][j] = temp
        
    return board

def right(board):
    for i in range(N):
        # 행 하나씩 확인
        target = N-1
        for j in range(N-2,-1,-1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                # 타켓이 0 일때
                if board[i][target] == 0:
                    board[i][target] = temp
                # 타겟이 현재 값과 같을 때 제곱하고 타겟 한칸 왼쪽
                elif board[i][target] == temp:
                    board[i][target] = temp*2
                    target-=1
                # 그 외라면 타겟 왼쪽 그자리에 현재 값 넣기
                else:
                    target-=1
                    board[i][target] = temp
        
    return board

def left(board):
    for i in range(N):
        # 행 하나씩 확인
        target = 0
        for j in range(1,N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                # 타켓이 0 일때
                if board[i][target] == 0:
                    board[i][target] = temp
                # 타겟이 현재 값과 같을 때 제곱하고 타겟 한칸 왼쪽
                elif board[i][target] == temp:
                    board[i][target] = temp*2
                    target+=1
                # 그 외라면 타겟 왼쪽 그자리에 현재 값 넣기
                else:
                    target+=1
                    board[i][target] = temp

    return board
             
ans = 0

def dfs(board,cnt):
    global ans

    if cnt == 5:
        ans = max(ans, max(map(max, board)))
        return
    
    dfs(up(deepcopy(board)),cnt+1)
    dfs(down(deepcopy(board)),cnt+1)
    dfs(right(deepcopy(board)),cnt+1)
    dfs(left(deepcopy(board)),cnt+1)

dfs(board,0)
print(ans)