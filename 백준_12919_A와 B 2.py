# 다시 풀어보기

import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

# S 1 , T 50 일때 2**50  -> X
answer = 0
N = len(S)

def check(str):
    global answer
    if str == S:
        answer = 1
        return
    if len(str) < N:
        return
    
    if str[0] == 'B':
        check(str[1:][::-1])
    if str[-1] == 'A':
        check(str[:-1])

check(T)
print(answer)

