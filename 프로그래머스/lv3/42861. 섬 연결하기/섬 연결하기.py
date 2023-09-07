def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2]) # 크루스칼 오름차순
    link = set([costs[0][0]]) # 시작지점
    
    while len(link) != n:
        for i in costs:
            a, b, cost = i
            # 두 섬이 이미 더 낮은 가격으로 연결이 되었을 경우 무시(오름차순)
            if a in link and b in link:
                continue
            # 두 섬 중 하나가 연결이 되어있지 않을 때 비용을 더하기
            if a in link or b in link:
                link.update([a,b])
                answer += cost
                break
    
    return answer