answer = 0

def solution(k, dungeons):
    global answer

    # 백트래킹으로 풀기
    
    visited = [False] * len(dungeons)
    
    def dfs(cnt, visited, k):
        global answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                dfs(cnt + 1, visited, k - dungeons[i][1])
                visited[i] = False
                
    dfs(0, visited, k)
    
    return answer