# 연산자 순열로 최대 최소 ㄱ계산?
# 정수 최대 100개라 ㄱㅊ할듯

import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
opcode = ['+','-','*','/']
ans = []

# 연산자 개수에 맞게 순열 구해주고 중복값 제거
p = ""
for i in range(4):
    p += op[i]*opcode[i]
for p in list(set(permutations(p))):

    # 순열 마다 값 계산
    temp = nums[0]
    for i in range(N-1):
        if p[i] == '+':
            temp += nums[i+1]
        elif p[i] == '*':
            temp *= nums[i+1]
        elif p[i] == '-':
            temp -= nums[i+1]
        elif p[i] == '/':
            temp = int(temp / nums[i+1]) # 버림 위해서 int 사용
    ans.append(temp)

# 최대 최소 출력
print(max(ans))
print(min(ans))