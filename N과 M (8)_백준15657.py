from itertools import combinations_with_replacement

N, M = map(int,input().split())
nums = list(map(int,input().split()))

for i in combinations_with_replacement(sorted(nums), M):
    print(' '.join(map(str, i)))
