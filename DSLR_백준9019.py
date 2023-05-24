import sys
from collections import deque

# bfs로 가능하다 bfs로 풀어봐야지 
# D는 *2해주고 9999보다 크면 10000로 나눈 나머지
# S는 -1을 뺀다. 0이면 9999저장
# L은 list(str())로 감싸서 swap해주고 join으로 다시 int로 변환
"""ex
A = list(str(A))
A[0],A[1],A[2], A[3] = A[3],A[0],A[1], A[2]
print(int(''.join(A)))
"""
# R도 같은 방법으로 
# 각각 결과를 반환하는 함수로 만들어서 활용하자

def commandD(n):
    n *= 2
    if n > 9999:
        n %= 10000
    return n

def commandS(n):
    n -= 1
    if n == -1:
        n = 9999
    return n

def commandL(n):
    n = list(str(n))
    # 자리수 맞춰주기
    while len(n) != 4:
        n.insert(0,'0')
    n[0],n[1],n[2], n[3] = n[1],n[2],n[3], n[0]
    n = int(''.join(n))
    return n

def commandR(n):
    n = list(str(n))
    # 자리수 맞춰주기
    while len(n) != 4:
        n.insert(0,'0')
    n[0],n[1],n[2], n[3] = n[3],n[0],n[1], n[2]
    n = int(''.join(n))
    return n

def bfs(A,B):
    q = deque()

    q.append((A,""))
    visited = set()
    visited.add(A)

    while q:
        n, ans = q.popleft()
        
        d = commandD(n)
        if d not in visited:
            if d == B:
                return ans+'D'
            q.append((d,ans+'D'))
            visited.add(d)

        s = commandS(n)
        if s not in visited:
            if s == B:
                return ans+'S'
            q.append((s,ans+'S'))
            visited.add(s)
        
        l = commandL(n)
        if l not in visited:
            if l == B:
                return ans+'L'
            q.append((l,ans+'L'))
            visited.add(l)

        r = commandR(n)
        if r not in visited:
            if r == B:
                return ans+'R'
            q.append((r,ans+'R'))
            visited.add(r)
        

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    print(bfs(A,B))
    #pypy3만 가능

