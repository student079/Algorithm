import sys

N, S = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

ans = []
res = 0
def dfs(start):
    global res

    if sum(ans) == S and len(ans) > 0:
        res += 1

    for i in range(start, N):
        ans.append(nums[i])
        dfs(i+1)
        ans.pop()
        
dfs(0)

print(res)