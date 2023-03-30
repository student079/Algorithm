import sys

k = int(sys.stdin.readline())
than = list(sys.stdin.readline().rstrip('\n').split())
visited = [False] * 10
maxres = ""
minres = ""

def check(i,j,k):
    if k == "<":
        return i < j
    else:
        return i > j
    
def dfs(step, s):
    global maxres, minres

    if(step == k + 1):
        if len(minres) == 0:
            minres = s
        else:
            maxres = s
        return
    
    for i in range(10):
        if not visited[i]:
            if(step == 0 or check(s[-1], str(i), than[step-1])):
                visited[i] = True
                dfs(step+1, s+str(i))
                visited[i] = False

dfs(0,"")
print(maxres)
print(minres)