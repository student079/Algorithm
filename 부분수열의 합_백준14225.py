import sys
from itertools import combinations

# 주어진 수열의 부분합으로 만들 수 있는 수 구하기
N = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))
comb = []
for i in range(1,N+1):
    for j in list(map(sum,combinations(S,i))):
        comb.append(j)

# 중복 제거
comb = list(set(comb))

# 1부터 확인하면서 만들 수 있는 수에 포함이 되는지 확인
i = 1
for c in sorted(comb):
    if c != i:
        print(i) # 중간에 없으면 만들 수 없는 수
        break
    i+=1
else :
    print(i) # 끝까지 있으면 그 다음 수