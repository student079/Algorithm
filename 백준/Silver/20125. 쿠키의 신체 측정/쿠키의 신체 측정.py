# 머리가 가장 위쪽 1칸
# 머리 바로 아래 심장
# 심장 왼쪽으로 가면 왼쪽 팔
# 심장 오른쪽으로 가면 오른쪽 팔
# 허리는 심장 아래 직선
# 왼쪽 다리는 허리 왼쪽 아래
# 오른쪽 다리는 허리 오른족 아래

#  N <= 1000

# 그리디
# 탐색?

# 초기화
import sys
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

# 머리 찾기
head = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            head = (i,j)
            break
    if head != 0:
        break

heart = (head[0]+1,head[1])

# 왼쪽 팔길이
leftArm = 0
for i in range(heart[1]-1,-1,-1):
    if board[heart[0]][i] == '*':
        leftArm+=1
    else:
        break
# 오른쪽 팔길이
rightArm = 0
for i in range(heart[1]+1,N):
    if board[heart[0]][i] == '*':
        rightArm+=1
    else:
        break

# 허리 길이
waist = 0
for i in range(heart[0] + 1,N):
    if board[i][heart[1]] == '*':
        waist+=1
    else:
        break

# 왼쪽 다리
leftLeg = 0
for i in range(heart[0] + waist+1,N):
    if board[i][heart[1] - 1] == '*':
        leftLeg+=1
    else:
        break

# 오른쪽 다리
rightLeg = 0
for i in range(heart[0] + waist+1,N):
    if board[i][heart[1] + 1] == '*':
        rightLeg+=1
    else:
        break

print(heart[0] + 1, heart[1] + 1)
print(leftArm, rightArm, waist, leftLeg, rightLeg)