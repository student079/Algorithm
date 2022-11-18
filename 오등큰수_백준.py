from sys import stdin
from collections import Counter

n = int(stdin.readline().strip("\n"))
arr = stdin.readline().strip("\n")
arr = arr.split(" ")
arr = list(map(int, arr))

# counter : 중복개수 튜플 형태로 구해줌 O(n)
cnt = Counter(arr)
res = [-1]*n

# 스택사용
stack = [0]
# arr[i]가 왼쪽들의 오등큰수인지 조사하고 arr[i]도 조사해야하기 때문에
# 끝나고 스택에 넣어줌
for i in range(1, n):
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        res[stack.pop()] = arr[i]

    stack.append(i)

print(*res)
