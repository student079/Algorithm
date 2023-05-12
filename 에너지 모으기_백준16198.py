import sys

N = int(sys.stdin.readline())
weights = list(map(int,sys.stdin.readline().split()))
# dfs로 백트래킹까지해서 완전탐색하자
# 그리디로 하니까 안풀림

answer = 0

def dfs(weights, res):
    global answer

    answer = max(answer,res)

    for i in range(1,len(weights)-1):
        dfs(weights[:i]+weights[i+1:],\
            res + weights[i-1] * weights[i+1])


for i in range(1,N-1):
    # 해당되는 요소 빼주고 넘기기
    dfs(weights[:i]+weights[i+1:], weights[i-1] * weights[i+1])

print(answer)