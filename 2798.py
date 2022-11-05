cards, M = map(int, input().split())
nums = [int(i) for i in input().split()]
result = []
for i in nums:
    for j in nums:
        for k in nums:
            if i == j or i == k or j == k:
                continue

            result_t = M-i-j-k
            if result_t >= 0:
                result.append(result_t)

print((M-min(result)))

# 라이브러리 사용법도 익히기