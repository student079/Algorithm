import sys
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())

s = [i for i in range(n+1)]

def find_repre(num):
    if s[num] != num:
        s[num] = find_repre(s[num])
    return s[num]

def union(num1, num2):
    num1 = find_repre(num1)
    num2 = find_repre(num2)
    if (num1 < num2):
        s[num2] = num1
    else:
        s[num1] = num2

for i in range(m):
    op, num1, num2=map(int, sys.stdin.readline().split())
    if op:
        if find_repre(num1) == find_repre(num2):
            
            print("yes")
        else:
            print("no")
    else:
        union(num1,num2)