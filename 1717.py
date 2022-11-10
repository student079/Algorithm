#disjoint

import sys
sys.setrecursionlimit(10**6); #재귀한도 늘리기

n,m=map(int, sys.stdin.readline().strip("\n").split());

set = [i for i in range(n+1)];

def find_repre(num):
    if set[num] != num:
        set[num] = find_repre(set[num]);
    return set[num];

def union(num1, num2):
    num1 = find_repre(num1);
    num2 = find_repre(num2);
    if (num1 < num2):
        set[num2] = num1;
    else:
        set[num1] = num2;

for i in range(m):
    op, num1, num2=map(int, sys.stdin.readline().strip("\n").split());
    if op:
        if find_repre(num1) == find_repre(num2):
            print("yes");
        else:
            print("no");
    else:
        union(num1,num2);
