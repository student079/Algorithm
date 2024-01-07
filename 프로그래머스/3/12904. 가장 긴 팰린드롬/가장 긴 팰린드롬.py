def solution(s):
    answer = 1

    S = len(s)
    for i in range(S-1):
        for j in range(i,S):
            if j - i + 1 > answer:
                str = s[i:j+1]
                if str == str[::-1]:
                    answer = max(answer,len(str))

    return answer