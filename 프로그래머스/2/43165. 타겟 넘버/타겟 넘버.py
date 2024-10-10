# 순서 바꾸지 않고 더하기 빼기만 해서 타겟넘버 만들기
# 방법의 수 return
# 완탐 가능한가?
# 20개
# 더하기 빼기 2**20 = 1048576 가능
# dfs

answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(index, s):
        if index == n:
            if s == target:
                global answer
                answer += 1
            return
        
        dfs(index+1, s + numbers[index])
    
        dfs(index+1, s + (numbers[index] * -1))
        
    dfs(0, 0)
    
    return answer