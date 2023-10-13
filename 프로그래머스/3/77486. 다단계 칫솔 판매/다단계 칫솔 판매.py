def solution(enroll, referral, seller, amount):
    # enroll로 딕셔너리 만들고
    # referral 있는 거 value로 넣기
    # 재귀하면서 나누기 10해서 root까지 들어가기
    # result에 합
    
    # 딕셔너리 만들기
    m = dict(zip(enroll,referral))
    sell_m = dict(zip(enroll, [0] * len(enroll)))
    
    # 판매 리스트 만들기
    seller = list(zip(seller, amount))
    
    # 판매 리스트 돌면서 재귀보고 answer에 합
    for p, c in seller:
        c =c*100
        while m[p] != '-':
            if c == 0: break
            sell_m[p] += c - c//10
            c = c//10
            p = m[p]
            
        sell_m[p] += c -c//10
        
    return list(sell_m.values())