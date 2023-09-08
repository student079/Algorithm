
def solution(info, edges):
    global answer
    answer = 0
    
    # 백드래킹?
    
    visited = [False] * len(info)
    
    def dfs(s, w):
        global answer
        
        if s > w:
            answer = max(answer, s)
        else:
            return
        
        for i in edges:
            p, c = i
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(s+1, w)
                else :
                    dfs(s, w+1)
                visited[c] = False
        visited[0] = True
    visited[0] = True
    dfs(1,0)
    return answer