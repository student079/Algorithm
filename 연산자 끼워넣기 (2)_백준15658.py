# 연산자 개수가 얼마나 클지 모르기 때문에
# 모듈써서 하면 시간초과 날듯
# dfs, 백트래킹으로 구하기

import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
maxAns = -1000000000 # 문제상황에서 최소값
minAns = 1000000000 # 문제 상황에서 최대값

# dfs 사용
def dfs(idx, ans):
    global maxAns, minAns

    # 모든 피연산자 사용 -> 종료
    if idx == N:
        maxAns = max(maxAns,ans)
        minAns = min(minAns,ans)
        return
    
    # 백트래킹
    if op[0] > 0:
        op[0] -= 1
        dfs(idx + 1, ans+nums[idx])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(idx + 1, ans-nums[idx])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(idx + 1, ans*nums[idx])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(idx + 1, int(ans/nums[idx]))
        op[3] += 1

# 처음 호출시에 ans에 첫번째 피연산자 넣어주기
dfs(1,nums[0])
print(maxAns)
print(minAns)