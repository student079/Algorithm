# 다시 풀어보기

from itertools import permutations

def solution(user_id, banned_id):
    
    answer = set()

    # 일단 경우의 수 다 뽑고
    b_len = len(banned_id)
    user_permutations = list(permutations(user_id, b_len))

    def check(users, banned):
        for i in range(b_len):
            l = len(users[i])
            if l != len(banned[i]):
                return False

            for j in range(l):
                if banned[i][j] == '*':
                    continue
                if users[i][j] != banned[i][j]:
                    return False
        return True


    for users in user_permutations:
        if check(users,banned_id):
            answer.add(tuple(sorted(users)))

    return len(answer)