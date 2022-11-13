#dynamic programing

import sys

def print_dp(lst,dp, i, max): #추가구현 
    if i == 0:
        print(lst[i],end="")
        return
    if max == dp[i]:
        print_dp(lst,dp,i-1,max-1)
        print(lst[i],end="")
    else :
        print_dp(lst,dp,i-1,max)


n = (int)(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
result=[]

dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j] and dp[i]< dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(max(dp))
print_dp(lst,dp,n-1,max(dp))

