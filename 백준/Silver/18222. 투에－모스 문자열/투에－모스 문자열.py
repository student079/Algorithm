# 홀수번째 수 // 2 반대
# 짝수번째 수 // 2

import sys

k = int(sys.stdin.readline())

def search(num):
    if num == 0:
        return False

    if num % 2 == 1:
        return not search(num//2)
    else:
        return search(num//2)

print(1 if search(k-1) else 0)

