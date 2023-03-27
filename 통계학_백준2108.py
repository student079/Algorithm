from sys import stdin
import collections

N = int(stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(stdin.readline()))

nums.sort()
print(int(round(sum(nums)/N,0)))
print(nums[(N//2)])
many = collections.Counter(nums).most_common(2)
if len(many) > 1 and many[0][1] == many[1][1]:
    many = many[1][0]
else:
    many = many[0][0]
print(many)
print(abs(nums[N-1] - nums[0]))