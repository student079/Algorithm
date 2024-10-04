# words 50개
# 단어길이 10개
# 완탐으로 다 들어가보기?
# 이미 본거는 안봐도댐
# 다 없다 ? 그럼 0
# 50 * 50

from collections import deque, defaultdict

def diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
    return count

def solution(begin, target, words):
    answer = 0
    n = len(words)
    
    q = deque()
    q.append((begin, 0))
    visited = defaultdict(lambda: False)
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            answer = count
            break
        
        for cand in words:
            if not visited[cand] and diff(word,cand) == 1:
                q.append((cand, count+1))
                visited[cand] = True
    
    return answer
