# 경우의 수
from collections import defaultdict

def solution(clothes):
    answer = 1
    cs = defaultdict(int)
    
    for c, t in clothes:
        cs[t] += 1
    
    for key in cs.keys():
        answer *= (cs[key] + 1)
    
    return answer - 1