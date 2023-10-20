# 다시 풀어보기

answer = 0

def is_diagonal_valid(qs, cnt, i):
    # 대각선 확인
    for j in range(cnt):
        # x증가량, y증가량 같은건 같은 대각선에 있는거
        # abs로 X자 대각선 커버 가능
        if abs(qs[j] - i) == abs(j - cnt):
            return False
    return True

def solution(n):
    
    
    qs = [-1] * n
    
    def dfs(qs, cnt):
        global answer
        if cnt == n:
            answer += 1
            return
        
        for i in range(n):
            if qs[cnt] != -1 or i in qs or not is_diagonal_valid(qs, cnt, i):
                continue
            qs[cnt] = i
            dfs(qs, cnt+1)
            qs[cnt] = -1
            
        return
    
    dfs(qs, 0)
    
    return answer