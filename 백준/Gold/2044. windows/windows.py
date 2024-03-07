#  window의 길이가 홀수인 경우 오른쪽이 왼쪽보다 하나 더 길다.
# 어떤 두 개의 window도 서로 겹치지 않게 배치되어 있다고 하자. 
# 모든 window의 가로, 세로 크기는 변하지 않아야 한다.
# 모든 window들은 title의 알파벳 순서로 정렬한다.
# 모든 window들을 왼쪽 위 꼭짓점이 화면 전체의 왼쪽 위 꼭짓점이 되도록 옮긴다
# 그리고 나서, 순서대로 한 칸씩 오른쪽 아래로 내려 배치한다.


import sys

M, N = map(int,sys.stdin.readline().split())
screen = []
for _ in range(M):
    screen.append(sys.stdin.readline().rstrip())

titles = []
# window 찾기
for i in range(M):
    # + 찾아서 title, 왼쪽 위 위치찾기
    a = -1
    for j in range(N):
        if screen[i][j] == '+':
            if a == -1:
                a = j
            else:
                temp = screen[i][a:j+1]
                if temp.count('|') :
                    s = ""
                    for t in temp:
                        if not (t == '+' or t == '-' or t == '|') :
                            s+=t
                    titles.append([s,temp, (i,a), len(temp)])# title,가로줄, 왼쪽 위 index, 가로길이
                a = -1
screen90 = list(map(list,zip(*screen)))
idx = 0
for title in titles:
    name, temp, index, w = title
    i ,j = index
    titles[idx].append(screen90[j][i+1:].index('+') + 2) # 세로길이
    idx+=1

# 배치
screen = [['.'] * N for _ in range(M)]
titles.sort()
for i in range(len(titles)):
    name, title, t, w, h = titles[i]
    screen[i][i:i+w] = title
    for x in range(i+1, i+h):
        for y in range(i, i+w):
            if (x == i + h - 1 and y == i) or (x == i + h - 1 and y == i+w-1):
                screen[x][y] = '+'
            elif y == i or y == i +w -1:
                screen[x][y] = '|'
            elif x == i + h - 1:
                screen[x][y] = '-'
            else :
                screen[x][y] = '.'
            
for i in screen:
    print("".join(map(str,i)))

    

