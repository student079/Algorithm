from collections import defaultdict

def solution(genres, plays):
    
    answer = []
    
    # 장르별 분류 dic
    gen = defaultdict(list)
    for i in range(len(plays)):
        gen[genres[i]].append((i, plays[i]))
    
    # 재생횟수 높은 장르로 정렬
    gen = sorted(gen.values(), key = lambda x : sum(y[1] for y in x), reverse = True)
    
    # 장르별로 재생횟수 높은거 정렬 후 최대 두개 인덱스 반환
    for g in gen:
        c = 0
        g.sort(key = lambda x: (x[1], -x[0]))
        while c < 2 and g:
            answer.append(g.pop()[0])
            c+=1
    return answer