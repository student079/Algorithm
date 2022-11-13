# 메모리 신경쓰기 *계수정렬
import sys

num = int(input())

lst = [0]*10001

for _ in range(num):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
