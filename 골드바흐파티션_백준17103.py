import sys

# 에라토스테네스의 체


N = int(sys.stdin.readline().rstrip('\n'))
nums = [int(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
m_num = max(nums)
prime = [True] * (m_num+1)
prime[0] = False
prime[1] = False

for i in range(2, int(m_num**0.5) + 1):
    if prime[i]:
        for j in range(i+i, m_num+1, i):
            prime[j] = False

for i in range(N):
    sum = 0
    for j in range(2, nums[i]//2 + 1):
        if prime[j] == 1 and prime[nums[i] - j] == 1:
            sum += 1
    print(sum)
