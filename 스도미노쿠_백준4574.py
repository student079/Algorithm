import sys


# 문제 이해 잘하자
# dfs 기본으로 박고 들어가면서

def is_valid(board, r, c, num):
    # 행과 열에 중복된 숫자가 있는지 확인
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    # 3x3 박스에 중복된 숫자가 있는지 확인
    box_row = (r // 3) * 3
    box_col = (c // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True

# 오른쪽이랑 아래만
dx = (1,0)
dy = (0,1)

# 출력 확인용
flag = False

def dfs(idx):
    global flag
    if idx == 81:
        if flag:
            flag = False
            # 스도미노쿠 퍼즐이 완성된 경우
            for row in board:
                print("".join(map(str,row)))
            return
        else:
            return
        
    x = idx//9
    y = idx%9

    if board[x][y] == 0:
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<9 and 0<=ny <9 and board[nx][ny] == 0:

                for i in range(1,10):
                    for j in range(i+1,10):
                        if (i,j) in domino:
                            continue
                        else:
                            # 블록 사용
                            if is_valid(board,x,y,i) and is_valid(board,nx,ny,j):
                                domino.append((i,j))
                                board[x][y] = i
                                board[nx][ny] = j
                                dfs(idx+1)
                                domino.remove((i,j))
                                board[x][y] = 0
                                board[nx][ny] = 0


                            if is_valid(board,x,y,j) and is_valid(board,nx,ny,i):
                                domino.append((i,j))
                                board[x][y] = j
                                board[nx][ny] = i
                                dfs(idx+1)
                                domino.remove((i,j))
                                board[x][y] = 0
                                board[nx][ny] = 0
    else:
        dfs(idx+1)
    


num = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    


    board = [[0]*9 for _ in range(9)]
    domino = [] # 사용한 블록
    for _ in range(N):
        temp = list(sys.stdin.readline().split())
        board[ord(list(temp[1])[0])-65][int(list(temp[1])[1])-1] = int(temp[0])
        board[ord(list(temp[3])[0])-65][int(list(temp[3])[1])-1] = int(temp[2])

        domino.append(tuple(sorted((int(temp[0]),int(temp[2])))))

    temp = list(sys.stdin.readline().split())
    for i in range(9):
        board[ord(list(temp[i])[0])-65][int(list(temp[i])[1])-1] = i+1
    print("Puzzle " + str(num))
    num+=1
    flag = True
    dfs(0)