# # numbers <= 100,000
# # 왼손, 오른손
# # dp

# def solution(numbers):
    
#     cost = [
#         [1, 7, 6, 7, 5, 4, 5, 3, 2 ,3], #0
#         [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], #1
#         [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], #2
#         [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], #3
#         [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], #4
#         [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], #5
#         [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], #6
#         [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], #7
#         [2, 5, 3, 5, 3, 2, 3, 2, 1, 2], #8
#         [3, 6, 5, 4, 5, 3, 2, 4, 2, 1] #9
#     ]
    
#     memo = dict()
#     memo[(4,6)] = 0
#     for num in numbers:
#         num = int(num)
#         currentMemo = dict()
        
#         for pos, weight in memo.items():
#             left, right = pos
            
#             if left == num:
#                 pass
#             elif right == num:
#                 pass
#             else:
#                 if (left, num) not in currentMemo.keys() or weight + cost[left][num] < currentMemo[(left,num)]
            
#         memo = currentMemo
        
        
        
#     return 0
costs =     [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
            ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
            ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
            ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
            ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
            ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
            ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
            ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
            ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
            ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

def solution(numbers):
    now_weight = 0
    left_pos = 4
    right_pos = 6
    all_dict = {}
    finger_pos = (left_pos, right_pos)
    all_dict[finger_pos] = now_weight
    
    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger_pos, weight in all_dict.items():
            left_pos, right_pos = finger_pos
            if right_pos == num:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + 1:
                    curr_dict[(left_pos, num)] = weight + 1
            elif left_pos == num:
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + 1:
                    curr_dict[(num, right_pos)] = weight + 1
            else:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + costs[right_pos][num]:
                    curr_dict[(left_pos, num)] = weight + costs[right_pos][num]
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + costs[left_pos][num]:
                    curr_dict[(num, right_pos)] = weight + costs[left_pos][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))