def solution(priorities, location):
    # location 인덱스에 있는 priority값 저장해놓고 -1로 변경
    target = priorities[location]
    priorities[location] = -1
    
    # priorities max랑 비교하면서 max값이 priority값이랑 비교
    count = 1
    while priorities:
        
    # priority보다 크면 그때 count
        pMax = max(priorities)
        if target > pMax:
            return count
        
    # priority보다 작으면 시뮬레이션 진행    
        elif target < pMax:
            while priorities:
                if priorities[0] == pMax:
                    priorities.pop(0)
                    count += 1
                    break
                else :
                    priorities.append(priorities.pop(0))
    
    # 같으면 앞에인덱스 중 max값과 같은 개수 만큼 count 증가
        else:
            for i in priorities:
                if i == -1:
                    return count
                elif i == target:
                    count += 1