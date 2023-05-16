import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

# DP 사용
# dpIncre : i번째 요소까지 포함했을 때 가장 긴 증가하는 수열 길이 저장
# dpDecre : i번째 요소까지 포함했을 때 가장 긴 감소하는 수열 길이 저장
dpIncre = [1] * N
dpDecre = [1] * N

for i in range(1,N):
    for j in range(i):
        if nums[i] > nums[j]:
            dpIncre[i] = max(dpIncre[i],dpIncre[j]+1)

# nums 뒤에서 부터 탐색
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if nums[i] > nums[j]:
            dpDecre[i] = max(dpDecre[i], dpDecre[j]+1)

ans = 0
# 둘의 합이 가장 큰것
# Sk가 두번 더해졌으므로 -1 해주기
for i in range(N):
    ans = max(ans,dpIncre[i]+dpDecre[i]-1)

print(ans)
        
