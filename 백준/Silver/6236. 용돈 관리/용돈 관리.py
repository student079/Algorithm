import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
moneys = []
for _ in range(N):
    moneys.append(int(sys.stdin.readline()))

# 이분탐색?

left = min(moneys)
right = sum(moneys)

answer = 0
while left <= right:
    mid = (left+right)//2
    
    cnt = 1
    balance = mid
    for money in moneys:
        if balance < money:
            cnt+=1
            balance=mid
        balance -= money
    
    if cnt > M or mid < max(moneys):
        left = mid+1
    else:
        right = mid - 1

print(left)