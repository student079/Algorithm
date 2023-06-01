import sys
from collections import deque
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
lab = []
for _ in range(N):
    lab.append(list(map(int,sys.stdin.readline().split())))

# N,M의 크기가 최대 8 이므로 시간은 크게 신경 안써도 될듯
# bfs로 바이러스 전파 구현가능
# 벽을 어떻게 세울ㄲ
# 조합으로 해보자
#  bfs로 바이러스 전파 시키고

# 일단 바이러스 좌표 구하기 + 0개수 + 벽 조합
virus = set()
zero = 0
wall = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.add((i,j))
        elif lab[i][j] == 0:
            wall.append((i,j))
            zero+=1
# 벽 조합 구하기
wall = list(combinations(wall,3))

zero -= 3 # 벽 세개 빼기

# bfs로 바이러스 전파
def bfs(virus,zero):
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    q = deque()
    visitedVirus = set()
    for i in virus:
        q.append(i)
        visitedVirus.add(i)
    while q:
        v = q.popleft()
        for k in range(4):
            nx = dx[k] + v[0]
            ny = dy[k] + v[1]

            if 0<= nx < N and 0<= ny < M \
                and lab[nx][ny] == 0 and (nx,ny) not in visitedVirus:
                visitedVirus.add((nx,ny))
                q.append((nx,ny))
                zero -= 1
    
    return zero

# 벽 조합에 맞춰서 해보기
ans = 0
for w1,w2,w3 in wall:
    lab[w1[0]][w1[1]] = 1
    lab[w2[0]][w2[1]] = 1
    lab[w3[0]][w3[1]] = 1
    ans = max(ans,bfs(virus,zero))
    lab[w1[0]][w1[1]] = 0
    lab[w2[0]][w2[1]] = 0
    lab[w3[0]][w3[1]] = 0


print(ans)

