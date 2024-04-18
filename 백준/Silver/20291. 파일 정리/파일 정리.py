# 파일을 확장자 별로 정리해서 몇 개씩 있는지
# 확장자들을 사전순
# N 1 ~ 50000
# 이름 소문자, 점(한번만) 3 ~ 100

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
appendixs = defaultdict(int)

# 파일 확장자만 떼기 100 * 50000
for _ in range(N):
    string = sys.stdin.readline().rstrip().split('.')
    appendixs[string[1]] += 1

# 딕셔너리에서 키 확장자 순 정렬 100 * 50000 * log 500000
for i in sorted(appendixs.keys()):
    print("{} {}".format(i, appendixs[i]))