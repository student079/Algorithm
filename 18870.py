# index는 오래걸림(리스트 처음부터 탐색)

import sys

item = int(sys.stdin.readline())

strs = sys.stdin.readline().strip("\n").split()

nums = []
for i in strs:
    nums.append(int(i))
nums = list(set(nums))
nums.sort()

nums_dict = {}

for i in range(len(nums)):
    nums_dict[nums[i]] = i

for i in strs:
    print("{}".format(nums_dict[int(i)]), end=" ")
