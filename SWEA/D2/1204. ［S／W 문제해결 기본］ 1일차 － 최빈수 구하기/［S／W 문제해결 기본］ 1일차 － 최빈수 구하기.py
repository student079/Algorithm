from collections import Counter

T = int(input())

for t in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    c = list(Counter(arr).most_common())
    c.sort(key= lambda x : (x[1], x[0]), reverse=True)
    print(f'#{n} {c[0][0]}')
