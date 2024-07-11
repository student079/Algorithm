# 교차하는 쌍
# N 500000
# 세그먼트 트리 구간합
import sys
from math import ceil, log

def update(left, right, node, idx):
    # 오른쪽 교차점 개수 구하기
    seg_tree[node] += 1
    if left == right:
        return 0
    mid = (left+right)//2

    if idx <= mid:
        return update(left, mid, node*2, idx) + seg_tree[node*2+1]
    else:
        return update(mid+1, right, node*2+1,idx)


N = int(sys.stdin.readline())
size = 2**(ceil(log(N, 2) + 1))
seg_tree = [0] + [0] * size
location = dict()
answer = 0

for i,a in enumerate(map(int, sys.stdin.readline().rstrip().split())):
    location[a] = i+1

for b in map(int,sys.stdin.readline().rstrip().split()):
    answer += update(1, N, 1, location[b])
print(answer)



