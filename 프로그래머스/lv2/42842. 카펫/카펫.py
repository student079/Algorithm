def solution(brown, yellow):
    
    # 완탐으로 가는데 가로세로를 완탐으로
    answer = []
    total = brown + yellow
    
    #가로세로 후보찾기
    for col in range(1,total+1):
        if total % col == 0:
            row = total / col
            if row * 2 + col * 2 - 4 == brown:
                answer = [row, col]
                
    return sorted(answer,reverse = True)