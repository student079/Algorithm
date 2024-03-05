# 인덱스
# 탐색?
# N <= 50
import sys

rank = 1
N, score, P = map(int,sys.stdin.readline().rstrip().split())
if N :
    rankingList = list(map(int,sys.stdin.readline().rstrip().split()))

# 랭킹 리스트가 꽉차면 새 점수가 이전 점수보다 좋을때만 점수가 바뀜
for i in range(N):
    if rankingList[i] <= score:
        rank = i+1
        if N == P and rankingList[N-1] == score:
            rank = -1
        break
else:
    if N == P :
        rank = -1
    else:
        rank = N+1

print(rank)