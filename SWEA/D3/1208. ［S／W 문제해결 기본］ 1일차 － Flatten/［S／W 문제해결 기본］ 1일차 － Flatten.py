

for t in range(1,11):
    d_cnt = int(input())
    heights = sorted(list(map(int, input().split())))

    for _ in range(d_cnt):
        heights[99] -= 1
        heights[0] += 1
        heights.sort()

    print(f'#{t} {abs(heights[99] - heights[0])}')


    