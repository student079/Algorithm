def solution(A, B):
    
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    
    a = 0
    for b in range(N):
        if A[a] < B[b]:
            answer+=1
            a+=1
            
    return answer