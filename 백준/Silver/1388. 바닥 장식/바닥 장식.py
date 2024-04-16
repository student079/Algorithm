# N, M 1 ~ 50
# 가로 모양, 세로 모양 찾기

# visited 관리
# 한칸씩 보면서 가로로 볼지 세로로 볼지 확인

import sys

N, M = map(int,sys.stdin.readline().rstrip().split())
room = []
for _ in range(N):
    room.append(list(sys.stdin.readline().rstrip()))
visited = [[False] * M for _ in range(N)]


def checkRow(i, j) -> None:

    visited[i][j] = True
    j += 1

    while j < M:

        if visited[i][j]:
            break

        if room[i][j] != '-':
            break
        
        visited[i][j] = True
        j += 1

def checkCol(i, j) -> None :
    visited[i][j] = True
    i += 1

    while i < N:

        if visited[i][j]:
            break

        if room[i][j] != '|':
            break
        
        visited[i][j] = True
        i += 1

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if room[i][j] == '-':
                checkRow(i, j)
                answer += 1
            else:
                checkCol(i, j)
                answer += 1

print(answer)