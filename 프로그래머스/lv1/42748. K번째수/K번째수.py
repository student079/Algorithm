def solution(array, commands):
    answer = []
    while commands:
        com = commands.pop(0)
        a = sorted(array[com[0]-1:com[1]])
        answer.append(a[com[2] -1])
        
    return answer