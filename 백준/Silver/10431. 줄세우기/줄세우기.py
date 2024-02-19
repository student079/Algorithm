# 20명

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):

    students = list(map(int,sys.stdin.readline().split()))[1:]
    res = 0
    line = [students[0]]
    cnt = 1
    for student in students[1:]:

        idx = 0
        while idx < cnt:
            if student < line[idx]:
                line.insert(idx,student)
                res += cnt - idx
                break
            idx += 1
        else:
            line.append(student)
        cnt += 1


    print(i, res)

