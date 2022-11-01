A = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
     "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
B = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
     "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

column, row = map(int, input().split())
chess = []
for i in range(column):  # 입력 받기
    chess.append(input())
cnt = []
for idxc in range(0, row-8+1):
    for idxr in range(0, column-8+1):
        temp_cntA = 0
        temp_cntB = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if chess[i+idxr][j+idxc] != A[i][j]:
                    temp_cntA += 1
                else:
                    pass
                if chess[i+idxr][j+idxc] != B[i][j]:
                    temp_cntB += 1
                else:
                    pass

        cnt.append(min(temp_cntA, temp_cntB))


print(min(cnt))
