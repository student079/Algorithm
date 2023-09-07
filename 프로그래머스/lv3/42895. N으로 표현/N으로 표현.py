def solution(N, number):
    
    # N으로 만들 수 있는 숫자를 연산 횟수 증가시키면서 구하기
    # 그게 number와 일치하면 그때의 숫자 리턴
    # 8까지 없으면 -1리턴
    
    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): # 1개부터 8개까지 확인
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1