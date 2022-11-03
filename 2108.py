# collections counter 사용 count 보다는

import sys
from collections import Counter

item = int(sys.stdin.readline())

lst = []
sum = 0
for i in range(item):
    lst.append(int(sys.stdin.readline()))
    sum += lst[i]

avg = round(sum/item)  # 평균

# 중앙값
lst.sort()
mid = 0
if item % 2 == 1:
    mid = lst[item//2]
else:
    mid = lst[item//2]+lst[item//2+1]//2

# 범위
r = max(lst)-min(lst)

# 최빈값


def mode(lstlst):
    cnt = Counter(lstlst).most_common()
    if len(cnt) == 1:
        return cnt[0][0]

    if cnt[0][1] == cnt[1][1]:
        return cnt[1][0]
    else:
        return cnt[0][0]


mode_num = mode(lst)


# 결과 출력

print(avg)
print(mid)
print(mode_num)
print(r)
