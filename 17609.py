# 문자열 슬라이싱 보다 인덱스로 접근이 빠름

import sys


def ispalin(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def isis(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            if ispalin(str, left+1, right) or ispalin(str, left, right-1):
                return 1
            return 2
    return 0


num = int(sys.stdin.readline())

for _ in range(num):
    strstr = str(sys.stdin.readline().strip())
    print(isis(strstr, 0, len(strstr)-1))
