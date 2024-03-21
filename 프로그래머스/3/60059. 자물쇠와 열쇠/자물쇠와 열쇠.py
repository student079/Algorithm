
def solution(key, lock):
    
    # 자물쇠 홈 개수가 키 홈 개수보다 작거나 같아야함
    # i,j에서 (-M<i,j<M) 키 인덱스 만큼 검사 
    # 회전까지
    # M ** 2 * 4 * N**2
    K = len(key)
    L = len(lock)
    answer = 0
    
    for i in range(L):
        for j in range(L):
            if lock[i][j] == 0:
                answer += 1
    
    def rotate(board):
        res = []
        for i in range(K-1, -1, -1):
            temp = []
            for j in range(K):
                temp.append(key[j][i])
            res.append(temp)
        return res
    
    for _ in range(4):
        key = rotate(key)
        
        up = set()
        for i in range(K):
            for j in range(K):
                if key[i][j] == 1:
                    up.add((i,j))
                    
        for i in range(-L+1,L):
            for j in range(-L+1,L):
                cnt = 0
                for pi, pj in up:
                    pi += i
                    pj += j
                    
                    if not (0<=pi<L and 0<=pj<L):
                        continue
                    
                    if lock[pi][pj] == 1:
                        break
                    
                    if lock[pi][pj] == 0:
                        cnt += 1
                else:    
                    if cnt == answer:
                        return True
    
    return False