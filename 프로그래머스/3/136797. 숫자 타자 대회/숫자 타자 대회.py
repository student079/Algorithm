# numbers <= 100,000
# 왼손, 오른손
# dp

def solution(numbers):
    
    cost = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2 ,3], #0
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], #1
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], #2
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], #3
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], #4
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], #5
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], #6
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], #7
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], #8
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1] #9
    ]
    
    memo = dict()
    memo[(4,6)] = 0
    for num in numbers:
        num = int(num)
        currentMemo = dict()
        
        for pos, weight in memo.items():
            left, right = pos
            
            if left == num :
                if (num,right) not in currentMemo.keys() \
                or currentMemo[(num,right)] > weight + 1:
                    currentMemo[(num,right)] = weight + 1
            elif right == num :
                if (left,num) not in currentMemo.keys() \
                or currentMemo[(left,num)] > weight + 1:
                    currentMemo[(left,num)] = weight + 1
                
            else:
                if (left, num) not in currentMemo.keys() \
                or weight + cost[right][num] < currentMemo[(left,num)]:
                    currentMemo[(left, num)] = weight + cost[right][num]
                if (num, right) not in currentMemo.keys() \
                or weight + cost[left][num] < currentMemo[(num, right)]:
                    currentMemo[(num, right)] = weight + cost[left][num]
            
        memo = currentMemo
        
    return min(memo.values())
