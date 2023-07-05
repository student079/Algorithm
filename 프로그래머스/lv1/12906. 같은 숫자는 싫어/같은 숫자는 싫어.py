def solution(arr):
    answer = []
    answer.append(arr[0])
    # O(n) 시간복잡도 가지는 게 좋을 듯
    for i in range(1,len(arr)):
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer