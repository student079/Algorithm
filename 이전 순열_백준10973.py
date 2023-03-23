import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

# 맨 뒤부터 탐색
for i in range(N-1, 0, -1):
    # 뒷 값이 앞 값보다 작으면
    if nums[i-1] > nums[i]:
        # 다시 뒤에서부터, 앞 값보다 큰 값이 있는지 탐색
        for j in range(N-1, 0, -1):
            # 뒷 값이 앞 값보다 작으면
            if nums[i-1] > nums[j]:
                # 두 값을 swap
                nums[i-1], nums[j] = nums[j], nums[i-1]
                # 뒷 값의 인덱스부터 끝까지 내림차순 정렬 후 출력
                nums = nums[:i] + sorted(nums[i:], reverse=True)
                print(" ".join(map(str, nums)))
                exit()
# 만약 뒷 값이 앞 값보다 작은 경우가 없다면, 맨 처음 순열이므로 -1
print(-1)