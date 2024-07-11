# 토핑개수 N 1~100

import sys

N = int(sys.stdin.readline())
cnt = 0
for item in set(sys.stdin.readline().rstrip().split()):
    # Cheese로 끝나는 것
    l = len(item)
    if l >= 6 and item[l-6:l] == "Cheese":
        cnt+=1
        if cnt >= 4:
            print("yummy")
            break
else:
    print("sad")