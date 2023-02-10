from sys import stdin

N ,M = map(int,stdin.readline().rstrip('\n').split())
paper = [0]*N

for i in range(N):
    paper[i]= list(map(int,stdin.readline().rstrip('\n').split()))

maxSum = 0
