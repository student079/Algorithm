gBeginning = None
gTarget = None
col, row = 0, 0
answer = float('inf')

def reverse(idx):
    if idx >= col:
        j = idx - col
        for i in range(col):
            gBeginning[i][j] = 1 - gBeginning[i][j]
    else:
        i = idx
        for j in range(row):
            gBeginning[i][j] = 1 - gBeginning[i][j]

def check():
    for i in range(col):
        for j in range(row):
            if gBeginning[i][j] != gTarget[i][j]:
                return False
    return True

def dfs(idx, depth = 0):
    global answer 
    if check():
        answer = min(answer, depth)
        return

    for i in range(idx + 1, col + row):
        reverse(i)
        dfs(i, depth + 1)
        reverse(i)

def solution(beginning, target):
    global gBeginning, gTarget, answer, col, row 
    gBeginning = beginning
    gTarget = target
    col, row = len(beginning), len(beginning[0])
    dfs(-1)
    return -1 if answer == float('inf') else answer