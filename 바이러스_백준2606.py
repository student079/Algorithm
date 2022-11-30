import sys
# 그래프 방식으로도 풀어보기


def disjoint(a, b):
    if arr[a] != arr[b]:
        temp1 = min(arr[a], arr[b])
        temp2 = max(arr[a], arr[b])
        arr[a] = temp1
        arr[b] = temp1
        for i in range(1, toCom+1):
            if arr[i] == temp2:
                arr[i] = temp1


toCom = int(sys.stdin.readline().rstrip('\n'))
edge = int(sys.stdin.readline().rstrip('\n'))

arr = list(range(toCom + 1))
arr[0] = toCom

for i in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    disjoint(a, b)

sum = -1
for i in arr:
    if i == 1:
        sum += 1

print(sum)
