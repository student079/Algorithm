import sys

N = int(sys.stdin.readline().rstrip())

numbers = []
i = 0
while 3**i <= N:
    numbers.append(3**i)
    i+=1

def dfs(res, idx):
    if N == 0:
        return False
    
    if idx == 0:
        return res == N
    return dfs(res + numbers[idx-1], idx-1) or dfs(res, idx-1)

print("YES") if dfs(0, len(numbers)) else print("NO")


