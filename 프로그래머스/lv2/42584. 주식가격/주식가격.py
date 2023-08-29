def solution(prices):
    
    # 인덱스랑 같이 저장해서 리턴하게끔
    # 스택에 넣고 스택 탑이랑 비교하면서 내려가면 pop해서 그 인덱스 랑 현재인덱스차이 넣기
    
    pLen = len(prices)
    answer = [0]*pLen
    stack = []
    
    # prices 만큼 돌면서
    for i in range(pLen):
        # stack 확인하고 stack top price 확인 후 가격이 내려갔으면
        while stack and stack[-1][1] > prices[i]:
            # pop해서 answer의 idx에 차이만큼 저장
            idx, price = stack.pop()
            answer[idx] = i-idx
        # 현재의 인덱스와 스택에 넣기
        stack.append((i, prices[i]))
    else :
        # 나머지 있는 것들 다 저장
        while stack:
            idx, price = stack.pop()
            answer[idx] = i-idx
    
    return answer