from itertools import permutations

def solution(user_id, banned_id):
    
    # 최대 8개 니까 유저들 중에 banned 길이 만큼 순열 뽑고
    # 솔팅 후에 셋에 저장
    # 셋 길이 리턴
    
    # 일치하는지 체크 함수
    def check(user, banned):
        if len(banned) != len(user):
            return False
        for idx in range(len(banned)):
            if banned[idx] == '*':
                continue
            if banned[idx] != user[idx]:
                return False
        return True
    
    # 순열 뽑기
    users = list(permutations(user_id, len(banned_id)))
    
    answer = set()
    for user_ids in users:
        cnt = 0
        for idx in range(len(banned_id)):
            if check(user_ids[idx], banned_id[idx]):
                cnt+=1
        if cnt == len(banned_id):
            answer.add(tuple(sorted(user_ids)))

    return len(answer)