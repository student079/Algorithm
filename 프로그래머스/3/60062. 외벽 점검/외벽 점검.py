# n이 원형
# permutation 사용
# permutation 사용없이 dfs로 구현해보자

from itertools import permutations

def solution(n, weak, dist):
    # weak 선형으로
    W = len(weak)
    weak = weak + [i+n for i in weak]
    
    answer = len(dist)+1
    
    for i,start in enumerate(weak[:W]):
        for members in permutations(dist):
            cnt = 1
            pos = start
            for member in members:
                pos += member
                if pos < weak[i + W - 1]:
                    cnt += 1
                    if cnt > answer:
                        continue
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    pos = [w for w in weak[i+1:i+W]
                                if w > pos][0]
                else :
                    answer = min(cnt, answer)
    
    return answer if answer != len(dist)+1 else -1