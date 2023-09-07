def solution(triangle):
    
    # 완탐 불가능 2^500
    
    h = len(triangle)
    
    for i in range(1, h):
        for j in range(i + 1):
            # 왼쪽 가
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            #오른쪽 가
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]) # 둘중 큰거
            
    return max(triangle[h-1])