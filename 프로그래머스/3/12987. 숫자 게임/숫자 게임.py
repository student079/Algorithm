def solution(A, B):
    
    # 대충 스택쓰는 느낌인데
    # B 정렬해서
    # 하나씩 확인하고 빼는 느낌으로 가자
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    a = 0
    b = 0
    for _ in range(N):
        if A[a] < B[b]:
            answer+=1
            b+=1
            a+=1
        else:
            b+=1
            
    return answer