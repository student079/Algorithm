import sys

N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

# N최대가 1,000,000이므로 O(n)시간복잡도를 갖는 로직으로 구현해야함
# 정렬 후에 각각 값에 맞는 idx를 갖는 딕셔러리에 넣어주자
d = dict()
Xcopy = sorted(set(X[:]))

idx = 0
for i in Xcopy:
    d[i] = idx
    idx+=1

for i in X:
    print(d[i],end=" ")
